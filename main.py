import sys
from analyzer import analyze_medicine_packet

def main():
    if len(sys.argv) > 1:
        # If an image path is passed as a command-line argument
        image_path = sys.argv[1]
        result = analyze_medicine_packet(image_path)
        print(result)
    else:
        print("Please provide an image path.")

if __name__ == "__main__":
    main()
