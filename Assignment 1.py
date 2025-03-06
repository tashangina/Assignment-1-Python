def main():
   
    names_input = input("Enter a list of names separated by commas: ")
    
    
    names_list = [name.strip() for name in names_input.split(',')]
    
   
    unique_names = set(names_list)
    
 
    sorted_names = sorted(unique_names)
    
   
    print("\nSorted Names:")
    for name in sorted_names:
        print(name)

    print("\nTotal number of unique names entered:", len(sorted_names))


if __name__ == "__main__":
    main()
