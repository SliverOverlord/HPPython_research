def main():

    with open("10x10_matrix.txt", "w") as f:
        
        for i in range(1, 101):
            if i % 10 == 0:
                f.write(str(i) + "\n")
            else:
                f.write(str(i) + " ")

        f.close()

if __name__ == "__main__":
    main()
