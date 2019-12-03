import json
import os


def main():
    """Export all the objects in samples file to json files in json subfolder."""
    # find current folder
    folder, file_name = os.path.split(__file__)
    # find all module names
    modules_names = [
        f[:-3] for f in os.listdir(folder)
        if f.endswith('.py') and f != file_name
    ]

    # load all the variables in each module and create a new json file for each
    for module_name in modules_names:
        module = __import__(module_name)
        samples = [name for name in dir(module) if not name.startswith('__')]
        for sample in samples:
            data = eval('module.%s' % sample)
            with open(os.path.join(folder, 'json', '%s.json' % sample), 'w') as outf:
                json.dump(data, outf, indent=4)
                print('exported {0} to /json/{0}.json'.format(sample))

if __name__ == '__main__':
    main()
