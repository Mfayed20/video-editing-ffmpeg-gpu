import subprocess
import shutil

# Check if ffmpeg is available in the system PATH
ffmpeg_path = shutil.which('ffmpeg')

if ffmpeg_path is None:
    print("Error: FFmpeg not found. Please install FFmpeg and add it to your system PATH.")
    exit(1)

# Rest of your code remains the same

# Command to overlay an image on a video and center it
command = [
    ffmpeg_path,  # Use the full path to ffmpeg
    '-i', './original/ori_video_hq.mp4',  # Input video file
    '-i', './original/ori_image_2x.png',  # Input image file
    '-filter_complex', '[1:v]scale=iw/2:ih/2[img];[0:v][img] overlay=(W-w)/2:(H-h)/2',  # Scale image and overlay it on video
    '-c:v', 'h264_nvenc',  # Video codec
    'output_with_image_centered_gpu.mp4'  # Output video file
]

# Execute the command
try:
    subprocess.run(command, check=True)
    print("Video processing completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error occurred while processing the video: {e}")
except FileNotFoundError:
    print("Error: FFmpeg executable not found. Please check your FFmpeg installation.")
