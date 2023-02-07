import os
import subprocess


def process_videos(input_folder, output_folder, compress_videos=False, compression_percentage=None,
                   watermark_file=None):
    # verifica se o arquivo de marca d'água foi fornecido
    if watermark_file is None:
        raise Exception("Watermark file not provided")
    # verifica se o arquivo de marca d'água existe
    if not os.path.exists(watermark_file):
        raise Exception("Watermark file not found")
    # verifica se o caminho da pasta de saída existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # loop pelos arquivos .mp4 na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename)
            # adiciona a marca d'água
            watermark_command = [
                "C:\\Users\\gusta\\PycharmProjects\\python-compress-video\\ffmpeg\\bin\\ffmpeg.exe",
                "-i", input_file,
                "-i", watermark_file,
                "-filter_complex",
                "overlay=main_w-overlay_w-300:main_h-overlay_h-50",
                output_file
            ]
            subprocess.call(watermark_command)
            # opcionalmente, comprima o vídeo
            if compress_videos:
                if compression_percentage is None:
                    compression_percentage = 50
                compression_command = [
                    "C:\\Users\\gusta\\PycharmProjects\\python-compress-video\\ffmpeg\\bin\\ffmpeg.exe",
                    "-i", output_file,
                    "-vcodec", "libx265",
                    "-crf", str(compression_percentage),
                    "-y",
                    output_file
                ]
                subprocess.call(compression_command)


def main():
    input_folder = "C:\\Users\\gusta\\PycharmProjects\\python-compress-video\\new\\input_teste"
    output_folder = "C:\\Users\\gusta\\PycharmProjects\\python-compress-video\\new\\output_teste"
    watermark_file = "./logo.png"
    compress_videos = True
    compression_percentage = 25
    process_videos(input_folder, output_folder, compress_videos, compression_percentage, watermark_file)


if __name__ == "__main__":
    main()
