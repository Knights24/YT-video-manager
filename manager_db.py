import sqlite3

conn = sqlite3.connect('youtube_manager.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXIST videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    pass

def add_videos():
    pass

def update_videos():
    pass

def delete_video():
    pass


def main():
    while True:

        print("\n Youtube Video Manager DB version")
        print("1. List all youtube videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")
        choice = input("Enter your choice : ")

        if choice == '1':
            list_videos()
        
        elif choice == '2':
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_videos(name,time)
        
        elif choice == '3':
            videoID = input("Enter the videoID to update : ")
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            update_videos(videoID,name,time)
        
        elif choice == '4':
            videoID = input("Enter the videoID to delete: ")
            delete_video(videoID)
        
        elif choice == '5':
            break
        
        else:
            print("Invalid Input")
    
    conn.close()

            



if __name__ == "__main__":
    main()