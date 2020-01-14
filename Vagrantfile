# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.require_version ">=1.7.0"

box = ENV['OVN_VAGRANT_BOX'] || "centos/8"


Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = box
  config.vm.synced_folder ".", "/vagrant", type: "rsync"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision.yml"
    ansible.compatibility_mode = "2.0"
    ansible.groups = {
      "ovn_central" => ["ovn0"],
      "ovn_nodes" => ["ovn1", "ovn2"],
      "ovn" => ["ovn0", "ovn1", "ovn2"]
    }
  end

  config.vm.define "ovn0", primary: true, autostart: true do |ovn0|
    ovn0.vm.hostname = "ovn0"
    ovn0.vm.network :public_network,
                    :mac => 'decaff000064',
                    :dev => 'virbr0',
                    :mode => 'bridge',
                    :type => 'bridge'
    config.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
      vb.customize ["modifyvm", :id, "--nictype2", "virtio"]
      vb.customize ["guestproperty", "set", :id,
                    "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000]
    end
  end
  config.vm.define "ovn1", primary: false, autostart: true do |ovn1|
    ovn1.vm.hostname = "ovn1"
    ovn1.vm.network :public_network,
                    :mac => 'decaff000065',
                    :dev => 'virbr0',
                    :mode => 'bridge',
                    :type => 'bridge'
    config.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
      vb.customize ["modifyvm", :id, "--nictype2", "virtio"]
      vb.customize ["guestproperty", "set", :id,
                    "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000]
    end
  end
  config.vm.define "ovn2", primary: false, autostart: true do |ovn2|
    ovn2.vm.hostname = "ovn2"
    ovn2.vm.network :public_network,
                    :mac => 'decaff000066',
                    :dev => 'virbr0',
                    :mode => 'bridge',
                    :type => 'bridge'
    config.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
      vb.customize ["modifyvm", :id, "--nictype2", "virtio"]
      vb.customize ["guestproperty", "set", :id,
                    "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000]
    end
  end
  config.vm.provider 'libvirt' do |lb|
      lb.disk_bus = "virtio"
      lb.nested = true
      lb.suspend_mode = 'managedsave'
      #lb.storage_pool_name = 'images'
  end
end
