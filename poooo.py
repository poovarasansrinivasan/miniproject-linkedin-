from linkedin_scraper import Person,Company, actions
from selenium import webdriver
driver = webdriver.Firefox()

email = ""
password = ""


def print_person(person):
    print("name "+person.name)
    print("url "+person.linkedin_url)
    # printing the list using loop
    for x in range(len(person.experiences)):
        print(person.experiences[x])
    for y in range(len(person.educations)):
        print(person.educations[y])

##################################
# main
##################################


def main():
    #
    # get image
    #
    actions.login(driver, email, password)  # if email and password is nt given, it'll prompt in terminal
    person = Person("https://www.linkedin.com/in/namachi", driver=driver)
    # a = Person("https://www.linkedin.com/in/sornam-arumugam-48943715", driver=driver)
    with open("output_data.csv", "w") as out_file:
        print_person(person)
        out_file.write(str(person))


##################################
# run
##################################
if __name__ == '__main__':
    main()
