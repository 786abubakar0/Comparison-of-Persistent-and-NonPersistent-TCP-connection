# Comparison-of-Persistent-and-NonPersistent-TCP-connection

In this comparison, the time taken by the persistent and non-persistent connection is compared for transferring 3 files from server to client that are a.jpg, b.mp3, c.txt. The comparison is done in Python 3.7 and results & conclusion is recorded in the file "report.pdf".  

Directories and files: 	
	
	**Place server.py and three files(a.jpg,b.mp3,c.txt) in the same directory. 
	**Make a folder named "persistent" where client-1 "client_persistent.py" is placed. (to store files served by server) 	
	**Make a folder named "non-persistent" where client-2 "client_nonpersistent.py" is placed. (to store files served by server) 	 
	
How to run: 	

	*First of all run server.py. 	
	*Enter port and ip for server. (1023 < port < 65535 since 0-1023 ports are dedicated ports) 	
	*If server and client are on same machine then ip can be 127.0.0.1 	
	*If server and client are on different machines, then the ip address can be gotten by writing "ipconfig" command on command prompt on windows  	
	**Then run any client (persistent or non-persistent) 	
	**provide server port and ip, that are specified in server.py. (ip and port where server is listening)  
	
Programs can be run on different machines but we need ip address to recognize that machine. We can test these programs on machines that are on same local networks. For devices on different networks, devices should have public ip address.

Comparison Conclusion:
	
	Thus from summary data in report.pdf, we can easily observe that in non-persistent http connection, the average time taken by each file or the average total time, are greater than the times in persistent http connection. The reason is in non-persistent, http connection for each file new connection has to be made while in persistent http connection only one connection has to be made for all files.
	In each connection creation, TCP has to perform 3-way handshake. So in non-persistent there is 3 times 3-way handshake while in persistent there is only one 3-way handshake.
	So the time is less in persistent http connection.

Note: The screenshots of scripts run (persisten_stats.png, non-persistent_stats.png, server.png) are just for reference purposes therefore the stats in "report.pdf" are different than that are showing in the images.
