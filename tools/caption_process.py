import tools.preprocess as preprocess
import json

class CaptionProcess(object):

    def __init__(self, source_data):
        self.source_data = source_data

    def process(self, do_sort=False, join_subtitles=True) -> list:
        course = open(self.source_data, 'r', encoding='utf-8').read()
        course = json.loads(course)
        result = []

        for key, value in course.items():
            video = {}
            video["title"] = key
            if not join_subtitles:
                video["subtitle_list"] = value
            else:
                video["subtitles"] = '\n'.join(value)
            result.append(video)

        if do_sort:
            result.sort(key=lambda x: x["title"])

        for idx, v in enumerate(result):
            v["index"] = idx
        return result


