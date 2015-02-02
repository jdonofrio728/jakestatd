# Author: Jacob D'Onofrio
# Date: May 2014

import java.lang.Integer as Integer
import java.lang.System as System
import java.lang.Exception as Exception

import java.rmi.Naming as Naming
import java.rmi.RMISecurityManager as RMISecurityManager
import java.rmi.registry.Registry as Registry
import java.rmi.registry.LocateRegistry as LocateRegistry
import java.rmi.server.UnicastRemoteObject as UnicastRemoteObject

import java.util.List as List

import sun.jvmstat.monitor.Monitor as Monitor
import sun.jvmstat.monitor.MonitoredHost as MonitoredHost
import sun.jvmstat.monitor.VmIdentifier as VmIdentifier
import sun.jvmstat.monitor.event.HostListener as HostListener
import sun.jvmstat.monitor.remote.RemoteHost as RemoteHost
import sun.jvmstat.monitor.remote.RemoteVm as RemoteVm
import sun.tools.jstatd.RemoteHostImpl as RemoteHostImpl

# JakeStatD Implementation
class JakeStatVmImpl(RemoteVm):
	_mvm = None
	def __init__(self, monitoredVm):
		print "Constructing JakeStat Remote VM Implementation instance"
		self._mvm = monitoredVm
	def getBytes(self):
		return self._mvm.getBytes()
	def getCapacity(self):
		return self._mvm.getCapacity()
	def detach(self):
		print "Calling detach()"
		self._mvm.detach()
	def getLocalVmId(self):
		return self._mvm.getVmIdentifier().getLocalVmId()
class JakeStatd(RemoteHost, HostListener):
	_monitoredHost = None
	_activeVms = None
	def __init__(self):
		try:
			self._monitoredHost = MonitoredHost.getMonitoredHost("localhost")
			self._activeVms = self._monitoredHost.activeVms()
			self._monitoredHost.addHostListener(self)
		except Exception, e:
			print "Werid issue occured"
			e.printStackTrace()
	def activeVms(self):
		print "Called activeVms()"
		mvs = None
		vmids = list()
		vms = self._monitoredHost.activeVms().toArray()
		for vm in vms:
			vmids.append(vm)
		return vmids
	def attachVm(self, lvmid, mode):
		print "Called attachVm " + str(lvmid) + " " + str(mode)
		v = Integer(lvmid)
		sb = "local://" + str(lvmid) + "@localhost"
		stub = None
		if mode != None:
			sb = sb + "?mode=" + mode
		try:
			vmid = VmIdentifier(sb)
			mvm = self._monitoredHost.getMonitoredVm(vmid)
			rvm = JakeStatVmImpl(mvm)
			stub = UnicastRemoteObject.exportObject(rvm, 2022)
		except Exception, e:
			print "Something went wrong while creating the RemoteVM"
			print str(e)
		return stub
	def detachVm(self,rvm):
		print "Called detachVm() "  + str(rvm)
		rvm.detach()
	def vmStatusChanged(self, event):
		print "Called vmStatusChanged() " + str(event)
		self._activeVms.retainAll(event.getActive())
	def disconnected(self, event):
		print "Should not occur!"

# Main
if System.getSecurityManager() == None:
	System.setSecurityManager(RMISecurityManager())

port = 2020
portOffset = port + 1
name = "//:" + str(port)+ "/JStatRemoteHost"
System.setProperty("java.rmi.server.ignoreSubClasses", "true")
#remote = RemoteHostImpl()
remote = JakeStatd()
stub = UnicastRemoteObject.exportObject(remote, portOffset)
try:
	Naming.rebind(name, remote)
except Exception, e:
	registry = LocateRegistry.createRegistry(port)
	Naming.rebind(name, remote)
print "Jakestatd is running"
