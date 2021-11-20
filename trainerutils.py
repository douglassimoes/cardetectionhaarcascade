import os


def generate_negative_description_file():
    # creates the negative image text file needed according to opencv documentation
    with open("negative.txt","w") as f:
        for filename in os.listdir("negative"):
            f.write("negative/"+filename+"\n")