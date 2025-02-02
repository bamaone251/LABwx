def generate_img_tags():
    print("Paste your list of links below (one link per line). When you're done, type 'END':")
    links = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        links.append(line.strip())

    print("\nGenerated HTML:")
    for link in links:
        print(f'<img src="{link}">')

# Call the function
generate_img_tags()
