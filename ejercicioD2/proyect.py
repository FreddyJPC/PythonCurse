try:
    with open('collaborators.txt', 'r') as file:
        collaborators = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    collaborators = []

print("The first 5 collaborators are:")
for i, collaborator in enumerate(collaborators[:5], start=1):
    print(f"{i}. {collaborator}")

new_collaborator = input("Enter the name of the new collaborator ")



if new_collaborator:
    if len(collaborators) < 15:
        if new_collaborator not in collaborators:
            collaborators.append(new_collaborator)
            with open('collaborators.txt', 'w') as file:
                for collaborator in collaborators:
                    file.write(f"{collaborator}\n")
            print(f"{new_collaborator} has been added")
    else:
        print("Cannot add more, the limit is 15.")


print("\nUpdated collaborators:")
for i, collaborator in enumerate(collaborators, start=1):
    print(f"{i}. {collaborator}")
