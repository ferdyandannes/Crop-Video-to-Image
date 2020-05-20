# Program To Read video 
# and Extract Frames 
import cv2
import os


# Function to extract frames
def check_dir(data_dir):
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable 
    count = 0

    # checks whether frames were extracted 
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames 
        success, image = vidObj.read()
        print(count)
        # Saves the frames with frame-count
        if(count == 0):
            save_dir = path.split(".")[0]
            check_dir(save_dir)
            check_dir(os.path.join(save_dir, "Images"))
        print(save_dir)
        save = os.path.join(save_dir, "Images/"+str(count).zfill(4)+".png")
        print(save)
        a = 585-385
        crop_img = image[a: a+385, 215: 1495]
        cv2.imwrite(save, crop_img)

        count += 1


# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("2.mp4")
