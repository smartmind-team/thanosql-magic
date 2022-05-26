import matplotlib.pyplot as plt
from IPython.display import Audio, Video, display
from matplotlib.pyplot import imread


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
        plt.axis("off")
        plt.imshow(image)
    plt.show()
    return


def print_audio(df, print_option):
    column = df.columns[0]
    audio_file_list = list(df[column])

    ### display 5 videos max
    limit = 5
    for audio in audio_file_list[:limit]:
        print(audio)
        display(Audio(audio))
    return


def print_video(df, print_option):
    column = df.columns[0]
    video_file_list = list(df[column])

    ### display 5 videos max
    limit = 5
    for video in video_file_list[:limit]:
        print(video)
        display(Video(video))
    return
