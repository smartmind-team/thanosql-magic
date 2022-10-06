import pandas as pd
from IPython.display import Audio, Image, Video, display
from psycopg2 import connect
from sqlalchemy import create_engine

from thanosql.exceptions import ThanoSQLInternalError
import warnings


def format_result(output_dict: dict):
    warnings.simplefilter(action='ignore', category=UserWarning)

    output_message = output_dict["data"]
    if not output_message.get("workspace_conn_info"):
        print("Success")
        return 
    workspace_conn_info = output_message["workspace_conn_info"]
    queries = output_message["query"]
    user = workspace_conn_info["user"]
    password = workspace_conn_info["password"]
    database = workspace_conn_info["database"]
    host = workspace_conn_info["host"]
    connection_string = f"postgresql://{user}:{password}@/{database}?host={host}"

    engine = create_engine(connection_string)
    conn = engine.connect()
    
    query_result = "Success"

    for query in queries:
        try:
            query_result = pd.read_sql_query(query, conn)
        except:
            pass
    
    print_type = output_message.get("print")
    if print_type:
        print_option = output_message.get("print_option", {})
        return print_result(query_result, print_type, print_option)

    return query_result


def print_result(query_df, print_type: str, print_option):
    if print_type == "print_image":
        return print_image(query_df, print_option)
    elif print_type == "print_audio":
        return print_audio(query_df, print_option)
    elif print_type == "print_video":
        return print_video(query_df, print_option)
    else:
        raise ThanoSQLInternalError("Error: Wrong print_type.")


def print_image(df, print_option):
    column_name = print_option.get("image_column", "image_path")
    image_file_list = list(df[column_name])

    base_dir = print_option.get("base_dir", "")
    limit = print_option.get("limit")
    for image_path in image_file_list[:limit]:
        image_full_path = f"{base_dir}/{image_path}"
        print(image_full_path)
        display(Image(image_full_path, width=240, height=240))
    return


def print_audio(df, print_option):
    column_name = print_option.get("audio_column", "audio_path")
    audio_file_list = list(df[column_name])

    base_dir = print_option.get("base_dir", "")
    limit = print_option.get("limit")
    for audio_path in audio_file_list[:limit]:
        audio_full_path = f"{base_dir}/{audio_path}"
        print(audio_full_path)
        display(Audio(audio_full_path))
    return


def print_video(df, print_option):
    column_name = print_option.get("video_column", "video_path")
    video_file_list = list(df[column_name])

    base_dir = print_option.get("base_dir", "")
    limit = print_option.get("limit")
    for video_path in video_file_list[:limit]:
        video_full_path = f"{base_dir}/{video_path}"
        print(video_full_path)
        display(Video(video_full_path, embed=True))
    return