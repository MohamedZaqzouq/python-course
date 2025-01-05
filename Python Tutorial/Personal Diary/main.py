file=open("diary.txt","a")
try:
    print("Enter the date (YYYY-MM-DD):")
    date=input()
    print("Enter your thoughts or experiences:")
    event=input()
    file.write(date+": "+event+"\n")
except IOError as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()

try:
    file=open("diary.txt","r")
    print("\nPrevious Entries:")
    print(file.read())
except FileNotFoundError:
    print("Diary file not found. Please create an entry first.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    file.close()