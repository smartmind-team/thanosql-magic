import matplotlib.pyplot as plt
from IPython.display import Audio, Video, display
from matplotlib.pyplot import imread


def print_image(df, print_option):
    w = 40
    h = 40
    fig = plt.figure(figsize=(w, h))

    column_name = df.columns[0]

    num_cols = 5
    num_rows = 5
    df = df[: num_cols * num_rows]
    base_path = print_option["base_path"]
    for idx, img_path in enumerate(df[column_name]):
        img_path = f"{base_path}/{img_path}"
        image = imread(img_path)
        fig.add_subplot(num_rows, num_cols, idx + 1)
        plt.axis("off")
        plt.title(img_path, fontdict={"fontsize": 50 / num_cols})
        plt.imshow(image)
    plt.show()
    return


def print_audio(df, print_option):
    column_name = df.columns[0]
    audio_file_list = list(df[column_name])

    ### display 5 videos max
    limit = 5
    base_path = print_option["base_path"]
    for aud_path in audio_file_list[:limit]:
        aud_path = f"{base_path}/{aud_path}"
        print(aud_path)
        display(Audio(aud_path))
    return


def print_video(df, print_option):
    column_name = df.columns[0]
    video_file_list = list(df[column_name])

    ### display 5 videos max
    limit = 5
    base_path = print_option["base_path"]
    for vid_path in video_file_list[:limit]:
        vid_path = f"{base_path}/{vid_path}"
        print(vid_path)
        display(Video(vid_path, embed=True))
    return
