from collections import defaultdict
from multiprocessing.sharedctypes import Value


# Solver that takes an input as a file object,
# and returns the output as a string
def solve(input):
    first_line = input.readline().strip().split(' ')
    nr_contributors = int(first_line[0])
    nr_projects = int(first_line[1])

    contributors = defaultdict(list)
    projects = defaultdict(dict)
    roles = defaultdict(list)

    # parsing contributors and skills
    for _ in range(nr_contributors):
        name, nr_skills = input.readline().strip().split(' ')

        # for each contributor
        for _ in range(int(nr_skills)):
            skill_name, skill_level = input.readline().strip().split(' ')
            contributors[name].append((skill_name, skill_level))
            roles[skill_name].append((name, skill_level))

    # for each project
    for _ in range(nr_projects):
        temp = input.readline().strip().split(' ')
        print(temp)
        name, completion, score, best_before, nr_roles = temp
        projects[name] = {
            'completion': completion,
            'score': score,
            'best_before': best_before,
            'nr_roles': int(nr_roles),
        }
        req_skills = []

        for _ in range(int(nr_roles)):
            skill_name, skill_level = input.readline().strip().split(' ')
            req_skills.append((skill_name, skill_level))

        projects[name]['req_skills'] = req_skills

    # Solution

    finalProjects = []
    for (name, data) in projects:
        chosenContributors = []
        for req_skill in data['req_skills']:
            contributor = min([x for x in roles[req_skill] if x[1] >= req_skill[1]], lambda:)
            chosenContributors.append(contributor)
        finalProjects.append((project, chosenContributors))

    output = f"""{len(finalProjects)}"""

    for (project, chosenContributors) in finalProjects:
        output += f"""\n{project}\n{" ".join(chosenContributors)}"""

    return output