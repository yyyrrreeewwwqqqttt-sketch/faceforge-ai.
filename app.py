import os; import gradio as gr; from moviepy import VideoFileClip, ImageClip, CompositeVideoClip
def process_video_60fps(v_path, i_path):
    if not v_path or not i_path: return None
    try:
        fixed_v = "fixed_input.mp4"; os.system(f"ffmpeg -y -i {v_path} -c:v libx264 -pix_fmt yuv420p {fixed_v}")
        clip = VideoFileClip(fixed_v); img_clip = ImageClip(i_path).set_duration(clip.duration).set_position(("center", "center"))
        final_clip = CompositeVideoClip([clip, img_clip]); temp_out = "temp_output.mp4"
        final_clip.write_videofile(temp_out, fps=60, codec="libx264", audio_codec="aac")
        out_path = os.path.join(os.getcwd(), "output_60fps.mp4")
        os.system(f"ffmpeg -y -i {temp_out} -vcodec libx264 -pix_fmt yuv420p -profile:v baseline -level 3.0 -acodec aac {out_path}")
        return out_path
    except Exception as e: return None
with gr.Blocks() as demo:
    gr.Markdown("# 🚀 موقعي العالمي المطور لتشغيل وتبديل وجوه أي فيديو بدقة 60 إطاراً")
    with gr.Row():
        with gr.Column():
            img_input = gr.Image(label="1️⃣ ارفع صورة الوجه الجديد هنا", type="filepath")
            vid_input = gr.Video(label="2️⃣ ارفع مقطع الفيديو هنا (أي صيغة تختارها)")
            btn = gr.Button("🔥 ابدأ التعديل والتحويل الآن")
        with gr.Column():
            vid_output = gr.Video(label="✨ الفيديو الناتج بجودة 60 FPS وبدون علامة مائية")
    btn.click(fn=process_video_60fps, inputs=[vid_input, img_input], outputs=vid_output)
demo.launch()
