from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

print("Loading model...")

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16
).to(device)

print("Model ready")

@app.get("/")
def home():
    return {"status": "Workout AI running"}

@app.post("/generate-summary")
async def generate_summary(data: dict):

    audience = data["audience"]
    workout = data["workout"]

    workout_lines = []

    for day, info in workout.items():

        exercise = info.get("exercise","")

        if "reps" in info:
            workout_lines.append(f"{day}: {exercise} {info['reps']} reps")

        elif "distance_km" in info:
            workout_lines.append(f"{day}: {exercise} {info['distance_km']} km")

        else:
            workout_lines.append(f"{day}: {exercise}")

    workout_text = "\n".join(workout_lines)

    if audience.upper() == "USER":
        temperature = 0.9  # Higher for more creative motivational summaries
        prompt = f"""You are a motivational fitness coach.

Write an encouraging summary of this week's workout.

Workout:
{workout_text}

Summary:"""

    else:
        temperature = 0.3  # Lower for factual, consistent coach summaries
        prompt = f"""You are a professional fitness coach.

Write a short factual workout report.

Workout:
{workout_text}

Summary:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    output = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=True,
        temperature=temperature,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

    generated = output[0][inputs["input_ids"].shape[1]:]

    result = tokenizer.decode(generated, skip_special_tokens=True)

    return {"summary": result}