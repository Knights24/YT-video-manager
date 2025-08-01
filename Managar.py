
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    pass

def add_videos(videos):
    pass

def delete_videos(videos):
    pass

def update_videos(videos):
    pass

def main():
    
    videos = load_data()

    while True:
        print("\n Youtube Video Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Delete a youtube video")
        print("4. Update a youtube video")
        print("5. Exit the app")
        choice =input("Enter your choice")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                delete_videos(videos)
            case "4":
                update_videos(videos)
            case "5":
                break
            case _:
                print("invalid")
        

if __name__ == "__main__":
    main()

   



    