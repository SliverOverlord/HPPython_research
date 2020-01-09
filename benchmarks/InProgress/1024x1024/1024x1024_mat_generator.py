def main():

    with open("1024x1024_matrix.txt", "w") as f:
        
        for i in range(1, 1048577):
            if i % 1024 == 0:
                f.write(str(i) + "\n")
            else:
                f.write(str(i) + " ")

        f.close()

if __name__ == "__main__":
    main()
