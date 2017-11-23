# -*- mode: ruby -*-
# vi: set ft=ruby :

# References
# https://www.vagrantup.com/docs/getting-started/provisioning.html
# https://github.com/FlipperPA/django-python3-vagrant/blob/master/Vagrantfile
# https://www.sitepoint.com/vagrantfile-explained-setting-provisioning-shell/
# http://kvz.io/blog/2013/01/16/vagrant-tip-keep-virtualbox-guest-additions-in-sync/
Vagrant.configure("2") do |config|
  # Environment setup
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine.
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  # Share an additional folder to the guest VM
  config.vm.synced_folder ".", "/vagrant", id: "vagrant-root", :mount_options => ["dmode=777","fmode=777"]

  # Install Python essentials
  config.vm.provision :shell, path: "scripts/vagrant.sh"
end