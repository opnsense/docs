![alt text](https://opnsense.org/wp-content/themes/OPNsense/assets/img/opnsense.png "Logo Title Text 1")

# OPNsense documentation
Welcome to the OPNsense documentation & wiki.   
The purpose of this project is to provide OPNsense users with quality documentation.

## Contribute
You can contribute to the project in many ways, e.g. testing
functionality, sending in bug reports or creating pull requests
directly via GitHub.  Any help is always very welcome!

## License
OPNsense documentation is available under the 2-Clause BSD license:

http://opensource.org/licenses/BSD-2-Clause

Every contribution made to the project must be licensed under the
same conditions in order to keep OPNsense truly free and accessible
for everybody.

Some pictures are licensed under the Creative Commons Zero (CC0) license:

https://creativecommons.org/publicdomain/zero/1.0/

Logo's may be subject to additional copyrights, property 
rights, trademarks etc. and may require the consent of a third party or the
license of these rights. Deciso B.V. does not represent or make any warranties
that it owns or licenses any of the mentioned, nor does it grant them.

#### Prepare build
Install Sphinx, our default theme and contrib packages
```
pip install -r requirements.txt
```


#### Generate HTML documents
```
make html
```

(```make clean``` to flush)


#### Changing theme
* Install Sass (http://sass-lang.com/),  on OSX via ```/Library/Ruby/Gems```
```
gem install --no-user-install sass
```
* Install npm (https://www.npmjs.com/get-npm)
* Install Bower (https://bower.io/)
```
npm install -g bower
```


Install required stylesheets using bower
```
bower install wyrm
bower install robotoslab-googlefont
bower install inconsolata-googlefont
bower install font-awesome#4.7.0
```
(for font-awesome, choose newest)


#### Build your theme:
```
sass -I bower_components/wyrm/sass/ -I bower_components/bourbon/dist/ -I bower_components/neat/app/assets/stylesheets/ -I bower_components/font-awesome/scss/ themes/opnsense/sass/theme.sass  > source/_static/css/opnsense.css
