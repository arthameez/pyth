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

curl --location --request POST '<route URL>:9200/insert-data' \
--form 'operation="insert"' \
--form 'city_id="1"' \
--form 'city="Abu Dhabi"' \
--form 'population="14910000"'

	
https://<route URL>/get-population

once completed you may delete VM - minishift delete -f --clear-cache

Removed cache content at: 'C:\Users\etisalat\.minishift\cache'
Removing entries from kubeconfig for cluster: 192-168-99-113:8443
Deleting the Minishift VM...
Minishift VM deleted.



Installing Helm into Minishift
==============================
Helm has two parts: a client (helm) and a server (tiller)
Tiller runs inside of your Kubernetes cluster, and manages releases (installations) of your charts.
Helm runs on your laptop, CI/CD, or wherever you want it to run.

Need to install Helm on your laptop, as it consists of two parts, a client (helm) and a server (tiller).



To find the latest client go to https://github.com/helm/helm/releases/tag/v3.9.0 <== Unpack the helm binary and add it to your PATH and you are good to go!

minishift install 

https://github.com/minishift/minishift/releases

https://cloud.redhat.com/blog/deploy-helm-charts-minishifts-openshift-local-development


helm install APP --host 192.168.99.103 --kube-context default/192-168-99-103:8443/system:admin

https://artifacthub.io/packages/helm/elastic/elasticsearch

helm repo add elastic https://helm.elastic.co

helm install elasticsearch --version 7.17.3 elastic/elasticsearch
helm install elasticsearch --version 7.17.3 elastic/elasticsearch  --kube-apiserver string localhost:8443



References:
==========

https://github.com/kadnan/Python-Elasticsearch/blob/master/fetch_recipes.py

code references -
https://collabnix.com/how-to-build-and-run-a-python-app-in-a-container/
https://github.com/noahgift/kubernetes-hello-world-python-flask/blob/main/app.py


Commands:
========
== Virtual BOX ==
https://www.virtualbox.org/wiki/Downloads 

https://www.osboxes.org/
https://www.osboxes.org/centos/ - download vdi image required for creating centos 

create new VM 

== Git hub ==

git init
git add -A (to add all)
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/arthameez/pyth.git

git push -u origin main
git remote -v
git remote add origin https://github.com/arthameez/pyth.git

git branch -M main
git push -u origin main

docker installation:
===================

https://repos.mirantis.com/centos/8/x86_64/test-20.10/Packages/

containerd.io-1.5.8-3.1.el8.x86_64.rpm
docker-ee-20.10.9-3.el8.x86_64.rpm
docker-ee-cli-20.10.9-3.el8.x86_64.rpm
container-selinux-2.9-4.el7.noarch.rpm


https://www.cyberithub.com/solved-failed-to-download-metadata-for-repo-appstream/ 
cd /etc/yum.repos.d/
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*


yum install policycoreutils-python
rpm -ivh container-selinux-2.9-4.el7.noarch.rpm
yum install container-selinux

rpm -ivh docker-ee-20.10.9-3.el8.x86_64.rpm
rpm -ivh docker-ee-cli-20.10.9-3.el8.x86_64.rpm
rpm -ivh docker-ee-20.10.9-3.el8.x86_64.rpm
yum install libcgroup
systemctl status docker
systemctl enable docker
systemctl start docker
docker ps

Docker registry = Public registry
https://hub.docker.com/
docker login arthameez/<>
docker pull arthameez/my-iamage:latest


Install Portainer
=================

docker pull portainer/portainer-ce:2.9.3
docker volume create portainer_data

docker run -d -p 8000:8000 -p 9443:9443 --name portainer \
    --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer-ce:2.9.3
