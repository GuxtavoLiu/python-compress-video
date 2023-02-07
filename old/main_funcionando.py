import subprocess


# funcionando, mas sem opacidade.
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


# compress_video("input.mp4", "output.mp4", 50, "watermark.png")
# compress_video("input.mp4", "output.mp4", 50, "watermark.png", duration=20, watermark_opacity=0.01)

compress_video("input.mp4", "output.mp4", "23", "watermark.png", watermark_opacity=0.1)
