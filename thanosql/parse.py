import re
from tkinter import W
from types import ModuleType
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
from ipywidgets import Audio, Video

def convert_local_ns(query_string, local_ns) -> str:
    # remove local_ns items with ModuleType
    local_ns = {
        key: val for key, val in local_ns.items() if not isinstance(val, ModuleType)
    }

    # variables need to be converted
    var_list = list(set(map(str.strip, re.findall(r"=( *?\w+)", query_string))))

    # modifying query_string
    for i in range(len(var_list)):
        var = local_ns.get(var_list[i])
        if var:
            query_string = query_string.replace(var_list[i], f"'{str(var)}'")

    return query_string

def print_image(df, print_option):
    w = 40
    h = 40
    fig = plt.figure(figsize=(w, h))
    columns = 10

    column = df.columns[0]
    rows = int(len(df[column]) / columns) + 1
    for i, img_path in enumerate(df[column]):
        image = imread(img_path)
        fig.add_subplot(rows, columns, i + 1)
        plt.axis('off')
        plt.imshow(image)
    plt.show()
    return

def print_audio(df, print_option):
    column = df.columns[0]
    audio_file = df[column][0]
    audio = Audio.from_file(audio_file)
    return audio 

def print_video(df, print_option):
    column = df.columns[0]
    video_file = df[column][0]
    video = Video.from_file(video_file)
    return video
 
def is_url(s):
    p = re.compile(r"^\w*://\w*")
    m = p.match(s)
    if m:
        return True
    else:
        return False

def split_string_to_query_list(s: str) -> list:
    """
    Split semi-colon containing string to query list and exclude empty string('').
    """
    return list(filter(None, map(lambda x: x.strip(), s.split(";"))))
