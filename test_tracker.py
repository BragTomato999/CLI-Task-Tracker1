import sys
import json

def main():
    if len(sys.argv) < 2:        # ← add this check
        print("Please provide a command")
        return

    file_path="C:\\Users\\ACER\\Desktop\\Python(BroCode)\\Projects\\task.json"
    command=sys.argv[1]

    

    if command=="add":
        print("You added")
        command2="".join(sys.argv[2]) #removes the spaces and make it is so that its one word
        print(f"Task added:{command2}")

        try:
            with open(file_path,"r") as file:
                tasks=json.load(file)
        except FileNotFoundError:
            tasks=[]

        task={
            "id":len(tasks)+1,
            "description":command2,
            "status":"todo",
        }
        tasks.append(task)

        with open(file_path,"w") as file:
            json.dump(tasks,file,indent=4)
            print(f"Task added successfully") 

    elif command=="delete":
        print("You deleted")
        command2=int(sys.argv[2])

        with open(file_path,"r") as file:
            contents=json.load(file)
            for task in contents:
                id_num=task["id"]
                if command2==id_num:
                    delete_content=task

            contents.remove(delete_content)
        
        with open(file_path,"w") as file:
            json.dump(contents,file)
            print("Succesfully deleted the Task")
        

    elif command=="list":
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                print(f"{task["id"]} {task["description"]}")    

    elif command=="update":
        command2=int(sys.argv[2])
        command3=sys.argv[3]
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                id_numm=task["id"]
                if command2==id_numm:
                    update_content=task

        update_content["description"] = command3   

        with open(file_path,"w") as file:
            json.dump(content,file)
        print("you have succesffuly changed the description")

    elif command=="mark_in_progress":
        command2=int(sys.argv[2])
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                id_num=task["id"]
                if command2==id_num:
                    update_content=task
        update_content["status"]="Task In Progess"
        with open(file_path,"w") as file:
            json.dump(content,file)
        print("You status was Changed")

    elif command=="task_done":
        command2=int(sys.argv[2])
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                id_num=task["id"]
                if command2==id_num:
                    update_content=task
        update_content["status"]="Task Completed"
        with open(file_path,"w") as file:
            json.dump(content,file)
        print("You status was Changed") 

    elif command=="list_to_do":    
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                status_code=task["status"]
                if status_code=="todo":
                    print(f"{task["id"]} {task["description"]} {task["status"]}")

    elif command=="list_task_completed":    
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                status_code=task["status"]
                if status_code=="Task Completed":
                    print(f"{task["id"]} {task["description"]} {task["status"]}")

    elif command=="list_in_progress":    
        with open(file_path,"r") as file:
            content=json.load(file)
            for task in content:
                status_code=task["status"]
                if status_code=="Task In Progress":
                    print(f"{task["id"]} {task["description"]} {task["status"]}")                    
    else:   
        print("Unknow command")                     
main()