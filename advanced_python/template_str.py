from string import Template

def main():
    # usual string formatting with format()
    str1 = "You're coding in {0} on {1}.".format("Python", "VS Code")
    print(str1)

    # create a template with placeholders
    templ = Template("You're coding in ${lang} on ${env}.")

    # use the subtitute method with keyword arguments
    str2 = templ.substitute(lang="Python", env="VS Code")
    print(str2)

    # use the substitude method with a dictionary
    # better security
    data = {
        "lang" : "Python",
        "env" : "VS Code"
    }

    str3 = templ.substitute(data)
    print(str3)


if __name__ == "__main__":
    main()