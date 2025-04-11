.. tabs::

    .. tab:: Organisation

        ================== ====================================================================================================
        **Option**         **Description**
        ================== ====================================================================================================
        **Enabled**        Enable this rule
        **Sort order**     The order in which rules are being processed.
        **Sequence**       The order in which rules are being processed. Please note that this is not a unique identifier, the
                           system will automatically recalculate the ruleset when rule positions are changed with the available
                           "Move rule before this rule" button.
        **Categories**     For grouping purposes you may select multiple groups here to organize items.
        **No XMLRPC Sync** Exclude this item from the HA synchronization process. An already existing item with the same UUID
                           on the synchronization target will not be altered or deleted as long as this is active.
        **Description**    You may enter a description here for your reference (not parsed).
        ================== ====================================================================================================

    .. tab:: Interface

        ==================== ====================================================================================================
        **Option**           **Description**
        ==================== ====================================================================================================
        **Invert Interface** Use all but selected interfaces
        **Interface**       
        ==================== ====================================================================================================

    .. tab:: Filter

        ====================== ====================================================================================================
        **Option**             **Description**
        ====================== ====================================================================================================
        **Quick**              If a packet matches a rule specifying quick, then that rule is considered the last matching rule and
                               the specified action is taken.             When a rule does not have quick enabled, the last
                               matching rule wins.
        **Action**             Choose what to do with packets that match the criteria specified below.             Hint: the
                               difference between block and reject is that with reject, a packet (TCP RST or ICMP port unreachable
                               for UDP) is returned to the sender, whereas with block the packet is dropped silently. In either
                               case, the original packet is discarded.
        **Allow options**      This allows packets with IP options to pass. Otherwise they are blocked by default.
        **Direction**          Direction of the traffic. The default policy is to filter inbound traffic, which sets the policy to
                               the interface originally receiving the traffic.
        **Version**           
        **Protocol**          
        **Invert Source**      Use this option to invert the sense of the match.
        **Source**            
        **Source Port**        Source port number or well known name (imap, imaps, http, https, ...), for ranges use a dash
        **Invert Destination** Use this option to invert the sense of the match.
        **Destination**       
        **Destination Port**   Destination port number or well known name (imap, imaps, http, https, ...), for ranges use a dash
        **Log**                Log packets that are handled by this rule
        **TCP flags**          Use this to choose TCP flags that must be set this rule to match.
        **TCP flags [out of]** Use this to choose TCP flags that must be cleared for this rule to match.
        **Schedule**          
        ====================== ====================================================================================================

    .. tab:: Stateful firewall

        ============================= ====================================================================================================
        **Option**                    **Description**
        ============================= ====================================================================================================
        **State type**                State tracking mechanism to use, default is full stateful tracking, sloppy ignores sequence numbers,
                                      use none for stateless rules.
        **State policy**              Choose how states created by this rule are treated, default (as defined in advanced),
                                      floating in which case states are valid on all interfaces or interface bound.             Interface
                                      bound states are more secure, floating more flexible
        **State timeout**             State Timeout in seconds (TCP only)
        **Adaptive Timeouts [start]** When the number of state entries exceeds this value, adaptive scaling begins. All timeout values are
                                      scaled linearly with factor (adaptive.end - number of states) / (adaptive.end - adaptive.start).
        **Adaptive Timeouts [end]**   When reaching this number of state entries, all timeout values become zero, effectively purging all
                                      state entries immediately. This value is used to define the scale factor, it should not actually be
                                      reached (set a lower state limit).
        **Max states**                Limits the number of concurrent states the rule may create.             When this limit is reached,
                                      further packets that would create state are dropped until existing states time out.
        **Max source nodes**          Limits the maximum number of source addresses which can simultaneously have state table entries.
        **Max source states**         Limits the maximum number of simultaneous state entries that a single source address can create with
                                      this rule.
        **Max source connections**    Limit the maximum number of simultaneous TCP connections which have completed the 3-way handshake
                                      that a single host can make.
        **Max new connections [c]**   Maximum new connections per host, measured over time.
        **Max new connections [s]**   Time interval (seconds) to measure the number of connections
        **Overload table**            Overload table used when max new connections per time interval has been reached.             The
                                      default virusprot table comes with a default block rule in floating rules,             alternatively
                                      specify your own table here
        **NO pfsync**                 This prevents states created by this rule to be synced with pfsync.
        ============================= ====================================================================================================

    .. tab:: Traffic shaping [experimental]

        ============================ ====================================================================================================
        **Option**                   **Description**
        ============================ ====================================================================================================
        **Traffic shaper**           Shape packets using the selected pipe or queue in the rule direction.
        **Traffic shaper [reverse]** Shape packets using the selected pipe or queue in the reverse rule direction.
        ============================ ====================================================================================================

    .. tab:: Source Routing

        ==================== ====================================================================================================
        **Option**           **Description**
        ==================== ====================================================================================================
        **Gateway**          Leave as 'default' to use the system routing table. Or choose a gateway to utilize policy based
                             routing.
        **Disable reply-to** Explicit disable reply-to for this rule
        **Reply-to**         Determines how packets route back in the opposite direction (replies), when set to default, packets
                             on WAN type interfaces reply to their connected gateway on the interface (unless globally disabled).
                             A specific gateway may be chosen as well here. This setting is only relevant in the context of a
                             state, for stateless rules there is no defined opposite direction.
        ==================== ====================================================================================================

    .. tab:: Priority

        ============================ ====================================================================================================
        **Option**                   **Description**
        ============================ ====================================================================================================
        **Match priority**           Only match packets which have the given queueing priority assigned.
        **Set priority**             Packets matching this rule will be assigned a specific queueing priority. If the             packet
                                     is transmitted on a vlan(4) interface, the queueing priority             will be written as the
                                     priority code point in the 802.1Q VLAN             header
        **Set priority [low-delay]** Used in combination with set priority, packets which have a TOS of lowdelay and TCP ACKs with no
                                     data payload will be assigned this priority when offered.
        **Match TOS / DSCP**        
        ============================ ====================================================================================================

    .. tab:: Internal tagging

        =================== ====================================================================================================
        **Option**          **Description**
        =================== ====================================================================================================
        **Set local tag**   Packets matching this rule will be tagged with the specified string.             The tag acts as an
                            internal marker that can be used to identify these packets later on.             This can be used,
                            for example, to provide trust between interfaces and to determine if packets have             been
                            processed by translation rules.  Tags are "sticky", meaning that the packet will be tagged even
                            if the rule is not the last matching rule.  Further matching rules can replace the tag with a
                            new one but will not remove a previously applied tag.  A packet is only ever assigned one tag at a
                            time.
        **Match local tag** Used to specify that packets must already be tagged with the given tag in order to match the rule.
        **Evaluations**    
        **States**         
        **Packets**        
        **Bytes**          
        **Icons**          
        =================== ====================================================================================================
