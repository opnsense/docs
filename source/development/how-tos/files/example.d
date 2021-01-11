
/* RX threads, retrieved from procstat -a -t, listing thread information for all (kernel) processes */
inline int	qg0 = 100018;
inline int	qg1 = 100019;
inline int 	qg2 = 100020;
inline int	qg3 = 100021;
inline int	qg4 = 100022;
inline int	qg5 = 100023;
inline int	qg6 = 100024;
inline int 	qg7 = 100025;

/* Because of this preprocessor statement, this script should be compiled with -C option */
#define PROBE_PREDICATE 		\
			pid == 0 &&	\
			(tid == qg0 || 	\
			 tid == qg1 || 	\
			 tid == qg2 || 	\
			 tid == qg3 || 	\
			 tid == qg4 || 	\
			 tid == qg5 || 	\
			 tid == qg6 || 	\
			 tid == qg7)	\
					\


#define DRIVER_CHECK self->driver_prefix == "ix"

/********************************************/
/* Iflib rx info & interrupt info */
/********************************************/

struct iflib_intr_info {
	uint64_t fast_intr_ts;
	uint64_t fast_intr_elapsed;
	uint64_t filter_routine_ts;
	uint64_t task_tx_ts;
};

struct iflib_intr_info ii[int];

struct iflib_task_info {
	uint64_t task_rx_ts; 
	uint64_t rxeof_ts;
};

struct iflib_task_info iti[int];

/* RX (and TX) interrupt entry point, will call driver supplied filter */
fbt::iflib_fast_intr:entry
{
	ii[tid].fast_intr_ts = timestamp;
	this->info = ((kernel`iflib_filter_info_t)arg0);
	self->rxq_id = (uint16_t)((kernel`iflib_rxq_t)this->info->ifi_ctx)->ifr_id;
	@intcounts[tid, self->rxq_id, probefunc] = count();

}

fbt::iflib_fast_intr:return
/ii[tid].fast_intr_ts/
{
	@time[tid, self->rxq_id, probefunc] = avg(timestamp - ii[tid].fast_intr_ts);
	@fi_time_min[tid, self->rxq_id, probefunc] = min(timestamp - ii[tid].fast_intr_ts);
	@fi_time_max[tid, self->rxq_id, probefunc] = max(timestamp - ii[tid].fast_intr_ts);
}

/* axgbe driver filter routine */
fbt::axgbe_msix_que:entry, fbt::ixgbe_msix_que:entry
{
	ii[tid].filter_routine_ts = timestamp;	
	@intcounts[tid, self->rxq_id, probefunc] = count();
}

fbt::axgbe_msix_que:return, fbt::ixgbe_msix_que:return
/ii[tid].filter_routine_ts/
{
	@fr_time_avg[tid, self->rxq_id, probefunc] = avg(timestamp - ii[tid].filter_routine_ts);
	@fr_time_min[tid, self->rxq_id, probefunc] = min(timestamp - ii[tid].filter_routine_ts);
	@fr_time_max[tid, self->rxq_id, probefunc] = max(timestamp - ii[tid].filter_routine_ts);
}


/* 
 * at this point, iflib has enqueued the _task_fn_rx / _task_fn_tx function,
 * we could measure some relevant things here.
 * The threads that run the queued functions are all in the range of the threads
 * defined at the top of this file
 * We could also inspect the queue structure to determine the average amount of functions
 * waiting to be serviced, this information could be pulled out of the iflib interrupt handler
 * Also, the thread that runs the queued function is different from the thread that runs the interrupt handler,
 * so query again for the relevant drivers and include it in the probe predicates
 */

char *driver_name[2];


fbt::_task_fn_rx:entry
/PROBE_PREDICATE && (!self->prefix_set)/
{


	/* get taskqueue structure information to determine amount of functions waiting to be serviced */
	this->rxq = ((kernel`iflib_rxq_t)arg0);
	this->grouptask = (struct grouptask)(this->rxq->ifr_task);
	self->gt_name = stringof(this->grouptask.gt_name);
	this->if_ctx = (if_ctx_t)(this->rxq)->ifr_ctx;
	this->dev = (device_t)(this->if_ctx)->ifc_dev;
	this->driver = (driver_t *)(this->dev)->driver;
	driver_name[0] = (const char *)(this->driver)->name;
	driver_name[1] = (const char *)(this->driver)->name + 1;
	self->driver_prefix = stringof(*(driver_name));
	self->prefix_set = 1;

}

fbt::_task_fn_rx:entry
/PROBE_PREDICATE && DRIVER_CHECK/
{
	iti[tid].task_rx_ts = timestamp;
	@_task_fn_rx_count[tid, self->gt_name, probefunc] = count();
}

fbt::_task_fn_rx:return
/PROBE_PREDICATE && iti[tid].task_rx_ts && DRIVER_CHECK/
{
	@task_rx_avg[tid, self->gt_name, probefunc] = avg(timestamp - iti[tid].task_rx_ts);
	@task_rx_min[tid, self->gt_name, probefunc] = min(timestamp - iti[tid].task_rx_ts);
	@task_rx_max[tid, self->gt_name, probefunc] = max(timestamp - iti[tid].task_rx_ts);
}


fbt::iflib_rxeof:entry
/PROBE_PREDICATE && DRIVER_CHECK/
{
	iti[tid].rxeof_ts = timestamp;
	@rxeof_count[tid, self->gt_name, probefunc] = count();

}

fbt::iflib_rxeof:return
/PROBE_PREDICATE && iti[tid].rxeof_ts && DRIVER_CHECK/
{
	@rxeof_avg[tid, self->gt_name, probefunc] = avg(timestamp - iti[tid].rxeof_ts);
	@rxeof_min[tid, self->gt_name, probefunc] = min(timestamp - iti[tid].rxeof_ts);
	@rxeof_max[tid, self->gt_name, probefunc] = max(timestamp - iti[tid].rxeof_ts);

}

fbt::ixgbe_isc_rxd_refill:entry
/PROBE_PREDICATE && DRIVER_CHECK/
{
	this->ts = timestamp;
	@rxd_refill_count[tid, self->gt_name, probefunc] = count();
}

fbt::ixgbe_isc_rxd_refill:return
/PROBE_PREDICATE && this->ts && DRIVER_CHECK/
{
	
	@rxd_refill_avg[tid, self->gt_name, probefunc] = avg(timestamp - this->ts);
	@rxd_refill_min[tid, self->gt_name, probefunc] = min(timestamp - this->ts);
	@rxd_refill_max[tid, self->gt_name, probefunc] = max(timestamp - this->ts);
}


/* notice how the ixgbe driver is missing, this is because of the dtrace compiler optimization - the return probe is missing */
fbt::ixgbe_isc_rxd_available:entry
/PROBE_PREDICATE && DRIVER_CHECK/
{
	this->ts = timestamp;
	@rxd_avail_count[tid, self->gt_name, probefunc] = count();
}

fbt::ixgbe_isc_rxd_available:return
/PROBE_PREDICATE && (this->ts != 0) && DRIVER_CHECK/
{
	@rxd_avail_avg[tid, self->gt_name, probefunc] = avg(timestamp - this->ts);
	@rxd_avail_min[tid, self->gt_name, probefunc] = min(timestamp - this->ts);
	@rxd_avail_max[tid, self->gt_name, probefunc] = max(timestamp - this->ts);
}

fbt::ixgbe_isc_rxd_pkt_get:entry
/PROBE_PREDICATE && DRIVER_CHECK/
{
	this->ts = timestamp;
	@rxd_pkt_get_count[tid, self->gt_name, probefunc] = count();
}

fbt::ixgbe_isc_rxd_pkt_get:return
/PROBE_PREDICATE && (this->ts != 0) && DRIVER_CHECK/
{
	@rxd_pkt_get_avg[tid, self->gt_name, probefunc] = avg(timestamp - this->ts);	
	@rxd_pkt_get_min[tid, self->gt_name, probefunc] = min(timestamp - this->ts);	
	@rxd_pkt_get_max[tid, self->gt_name, probefunc] = max(timestamp - this->ts);	
}


/********************************************/
/* Queue behaviour */
/********************************************/

int qlen[int];

/* enqueue and deqeueue probes to determine the run length of the queues */
sched:::enqueue
/PROBE_PREDICATE && DRIVER_CHECK/
{
	this->q_len = qlen[tid]++;

	@q_len_all_threads_avg[tid] = avg(this->q_len);
	@q_len_all_threads_min[tid] = min(this->q_len);
	@q_len_all_threads_max[tid] = max(this->q_len);
}

sched:::dequeue
/PROBE_PREDICATE && qlen[tid] && DRIVER_CHECK/
{
	qlen[tid]--;

}


END
{
	printf("\n");
	printf("\n");
	printf("\n");
	printf("\n");
	printf("-------INTERRUPTS-------\n");
	printf("\n");
	printf("thread  core               function            count  avg time(ns)  min time  max time  avg time(driver)  min time(driver)  max time(driver)\n");
	printf("------  ----  ---------------------  ---------------  ------------  --------  --------  ----------------  ----------------  ----------------\n");
	printa("%6d  %4d  %21s  %@15d  %@12d  %@8d  %@8d  %@16d  %@16d  %@16d\n", @intcounts, @time, @fi_time_min, @fi_time_max, @fr_time_avg, @fr_time_min, @fr_time_max);
	printf("\n");

	printf("-------DRIVER/IFLIB FUNCTIONS RX-------\n");
	printf("thread  grouptask name                        function  avg time(ns)  min time(ns)  max time(ns)        count\n");
	printf("------  --------------  ------------------------------  ------------  ------------  ------------  -----------\n");
	printa("%6d  %14s  %30s  %@12d  %@12d  %@12d  %@11d\n", @task_rx_avg, @task_rx_min, @task_rx_max, @_task_fn_rx_count);
	printa("%6d  %14s  %30s  %@12d  %@12d  %@12d  %@11d\n", @rxeof_avg, @rxeof_min, @rxeof_max, @rxeof_count);
	printa("%6d  %14s  %30s  %@12d  %@12d  %@12d  %@11d\n", @rxd_refill_avg, @rxd_refill_min, @rxd_refill_max, @rxd_refill_count);
	printa("%6d  %14s  %30s  %@12d  %@12d  %@12d  %@11d\n", @rxd_avail_avg, @rxd_avail_min, @rxd_avail_max, @rxd_avail_count);
	printa("%6d  %14s  %30s  %@12d  %@12d  %@12d  %@11d\n", @rxd_pkt_get_avg, @rxd_pkt_get_min, @rxd_pkt_get_max, @rxd_pkt_get_count);
	printf("\n");


	printf("---------QUEUE BEHAVIOUR---------\n");
	printf("thread  avg run length  min run length  max run length\n");
	printf("------  --------------  --------------  --------------\n");
	printa("%6d  %@14d  %@14d  %@14d\n", @q_len_all_threads_avg, @q_len_all_threads_min, @q_len_all_threads_max);
	printf("\n");
}

