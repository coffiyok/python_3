from FileManager import FileManager
from DataLoader import DataLoader
from analyzer import analyzer
from ResultSave import ResultSave


def main():
    data_file = "students.csv"

    fm = FileManager(data_file)
    if not fm.check_file():
        print("Stopping program.")
        return
    fm.create_output_folder()

    dl = DataLoader(data_file)
    dl.load()
    dl.preview()

    analyser = analyzer(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSave(analyser.result, 'output/result.json')
    saver.save_json()


if __name__ == "__main__":
    main()