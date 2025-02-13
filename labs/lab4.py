import subprocess
import os




def task1():
    try:
        

        p=subprocess.run(["wsl", "ls", "-a", "-l", "/var/log"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
        err_b=p.stderr
        err_str=err_b.decode()
        print(err_str)
        
        output_b=p.stdout
        output_str=output_b.decode()
        #print(output_b)
        print(output_str)
        print("ls -a -l /var/log")
    except FileNotFoundError:
        print("file or command not found ")
        # print(p.stderr.decode())
    except PermissionError:
        print("Premisson denied use sudo") 
        # print(p.stderr.decode())

    print(p.returncode)
    
    
    
def task2():
        try:
            cmd="systemctl status nginx"
            p=subprocess.run(["wsl", "sudo", "systemctl", "status", "nginx"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print(p.returncode)
            if p.returncode==0:
                print(p.stdout.decode())
                print("Nginx is running ")
            else:    
                print("Ngix is not runnig")
        except PermissionError:
            print("Premisson denied use sudo") 



task2()        