import wikipedia

input_text = "\n>>> "

def random():
    random_pages = wikipedia.random(pages=10)
    for page in random_pages:
        print(page)


def search_pages(query):
    titles = wikipedia.search(query, results=5)
    if not titles:
        print("I couldn't find any matching Wikipedia pages.")
        return None

    print("\nPlease choose a page:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")

    while True:
            page_choice = int(input(input_text))
            selected_title = titles[page_choice - 1]
            page = wikipedia.page(selected_title, auto_suggest=False)
            return page


def chatbot():
    while True:
        print("Enter a search term. Type 'random' for 10 random articles. To leave, type 'exit' or 'quit'.\n")
        user_input = input(input_text)
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        elif user_input.lower() in ["random"]:
            random()
        else:
            page = search_pages(user_input)
            summary = page.summary
            sections = page.sections
            if page:
                while True:
                    print("\nChoose an option:")
                    print("1. Page Summary")
                    print("2. Page Sections")
                    print("3. Page Links")
                    print("0. Back")

                    choice = input(input_text).strip()

                    if choice == "0": # Exit to main chatbot loop for a new search
                        break  
                    elif choice == "1": # Page Summary
                        print("Summary for '" + page.title + "':")
                        print(summary)
                    elif choice == "2": # Page sections
                        while True:
                            print("\nSections for '" + page.title + "':")
                            for i, section in enumerate(sections, 1):
                                print(f"{i}. {section}")
                            print("0. Back")
                            section_choice = int(input(input_text))
                            if section_choice == 0: # Show the menu again
                                break  
                            elif 1 <= section_choice <= len(sections):
                                section = sections[section_choice - 1]
                                print(f"\n{page.title} : {section}\n")
                                print(page.section(section))
                                break
                    elif choice == "3":
                        print("Links for '" + page.title + "':")
                        print(page.links)

chatbot()
