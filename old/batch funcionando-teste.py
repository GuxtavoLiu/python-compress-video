import os
import subprocess
import time
from tqdm import tqdm


def batch_compress_and_watermark(input_folder, output_folder, compression_percentage, watermark_file):
    video_files = [file for file in os.listdir(input_folder) if file.endswith(".mp4")]
    total_files = len(video_files)
    start_time = time.time()
    for index, file in enumerate(video_files):
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file)
        pbar = tqdm(total=1, unit='files', desc=file)
        compress_video(input_file, output_file, compression_percentage, watermark_file)
        pbar.update(1)
        pbar.close()

        # Calculate estimated time remaining
        elapsed_time = time.time() - start_time
        remaining_files = total_files - (index + 1)
        estimated_time_remaining = elapsed_time * remaining_files / (index + 1)

        # Update overall progress bar
        overall_pbar.update(1)
        overall_pbar.set_description("Time remaining: {:.2f}s".format(estimated_time_remaining))
    overall_pbar.close()

def compress_video(input_file, output_file, compression_percentage, watermark_file, duration=None,
                   watermark_opacity=0.3):
    compression_percentage = str(compression_percentage) + "%"
    filter_complex = "overlay=main_w-overlay_w-30:main_h-overlay_h-30,format=rgba,colorchannelmixer=aa={}[watermarked]".format(
        watermark_opacity)
    if duration:
        filter_complex = "overlay=main_w-overlay_w-30:main_h-overlay_h-30:enable='between(t,0,{})',format=rgba,colorchannelmixer=aa={}[watermarked]".format(
            duration, watermark_opacity)
    subprocess.run(
        ["C:\\ffmpeg\\bin\\ffmpeg.exe", "-i", input_file, "-i", watermark_file, "-filter_complex", filter_complex,
         "-map", "[watermarked]", "-map", "0:a", "-c:v", "libx264", "-crf", "24", "-y", output_file])

overall_pbar = tqdm(total=len([file for file in os.listdir('C:\\Users\\Tracker\\PycharmProjects\\python-compress-video') if file.endswith(".mp4")]), unit='files', desc='Overall Progress')
batch_compress_and_watermark('C:\\Users\\Tracker\\PycharmProjects\\python-compress-video', "C:\\Users\\Tracker\\PycharmProjects\\python-compress-video\\compress", 50,
                             "watermark.png")
