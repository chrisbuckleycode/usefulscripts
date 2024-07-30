// Info CLI tool for Linux/Unix (due to simple clear screen hack)
// Some lines are commented out due to currently unused pakages/functions/metrics (take up a lot of screen estate by default)
//
// Instructions:
// go mod init example.com/cli-info
// go mod tidy
// go run cli_info.go


package main

import (
	"fmt"
	"time"

	"github.com/shirou/gopsutil/v3/cpu"
	"github.com/shirou/gopsutil/v3/disk"
	"github.com/shirou/gopsutil/v3/host"
	"github.com/shirou/gopsutil/v3/load"
	"github.com/shirou/gopsutil/v3/mem"
	"github.com/shirou/gopsutil/v3/net"
	//"github.com/shirou/gopsutil/v3/process"
)

func main() {
	for {
		// CPU metrics
		cpuPercent, _ := cpu.Percent(time.Second, false)
		cpuCounts, _ := cpu.Counts(false)
		//cpuTimes, _ := cpu.Times(false)

		// Memory metrics
		memory, _ := mem.VirtualMemory()
		swapMemory, _ := mem.SwapMemory()

		// Disk metrics
		//partitions, _ := disk.Partitions(false)
		diskUsage, _ := disk.Usage("/")
		//diskIOCounters, _ := disk.IOCounters()

		// Host metrics
		hostInfo, _ := host.Info()
		hostUsers, _ := host.Users()

		// Load metrics
		loadAvg, _ := load.Avg()

		// Network metrics
		netIOCounters, _ := net.IOCounters(false)
		//netConnections, _ := net.Connections("all")

		// Process metrics
		//processes, _ := process.Processes()

		// Display metrics
		fmt.Printf("CPU Usage: %.2f%%\n", cpuPercent[0])
		fmt.Printf("CPU Counts: %d\n", cpuCounts)
		// fmt.Printf("CPU Times: %+v\n", cpuTimes)
		fmt.Printf("Memory Usage: %.2f%%\n", memory.UsedPercent)
		fmt.Printf("Swap Memory Usage: %.2f%%\n", swapMemory.UsedPercent)
		// fmt.Printf("Disk Partitions: %+v\n", partitions)
		fmt.Printf("Disk Usage: %+v\n", diskUsage)
		//fmt.Printf("Disk IO Counters: %+v\n", diskIOCounters)
		fmt.Printf("Host Info: %+v\n", hostInfo)
		fmt.Printf("Host Users: %+v\n", hostUsers)
		fmt.Printf("Load Average: %+v\n", loadAvg)
		fmt.Printf("Network IO Counters: %+v\n", netIOCounters)
		//fmt.Printf("Network Connections: %+v\n", netConnections)
		//fmt.Printf("Processes: %+v\n", processes)

		// Refresh (i.e. wait) after X seconds		
		time.Sleep(5 * time.Second)

		// Clear screen hack for Linux/Unix
		fmt.Println("\033[2J")
	}
}
