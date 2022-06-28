Project details are placed at - https://github.com/arthameez/pyth.git

Prerequisites:
=============

Require a system with minimum 4 core cpu 8 GB RAM and 128 GB HDD

Tools Required:
==============

1> VMware virtual box => https://www.oracle.com/ae/virtualization/technologies/vm/downloads/virtualbox-downloads.html
(install it by double clicking the application and from task manager -> CPU verify that virualisation is enabled )
2> Minishift => https://github.com/minishift/minishift/releases 
(extract this in a folder)
3> windows CMD - command line interface or powershell

Depoyment Procedure:
===================
1> Open CMD - run as administartar
2> cd to the folder where minishift is extracted
3> start minishift by executing -> 
		minishift config set vm-driver virtualbox (to set virtualbox driver)
		minishift start --vm-driver virtualbox (this will take around 10 minutes and it will give details about console)
		The server is accessible via web console at:
			https://192.168.99.100:8443/console

		You are logged in as:
			User:     developer
			Password: <any value>

		To login as administrator:
			oc login -u system:admin

4> login to above console as (system/admin)
5> after login create a new project and name it as (my project)
6> go to the create project space and select import from yaml and paste contents of elasticttemplate.yml from git -> https://github.com/arthameez/pyth
this will install an elasticsearch instance with 1 replica and service name a elastic search
for smooth build, you may load the image as
minishift ssh
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.2.3
7> now go to add to project (same project i.e my-project -> from catalog -> select python -> git url -> paste (https://github.com/arthameez/pyth.git) -> provide app name as my-app
this will install the applicaiton with 1 replica ,  service and  routs will be created
Note - you may get ureferenced brach master, go to build and in the configuration of git change from master to main and rebuild
8> access the applicaiton with three URL - application routs-> you will find by default a URL hit on it will take you to index page , alter other URL as per application example below

https://<route URL>/healthz
https://<route URL>/insert-data
https://<route URL>/get-population

once completed you may delete VM - minishift delete -f --clear-cache

Removed cache content at: 'C:\Users\etisalat\.minishift\cache'
Removing entries from kubeconfig for cluster: 192-168-99-113:8443
Deleting the Minishift VM...
Minishift VM deleted.
