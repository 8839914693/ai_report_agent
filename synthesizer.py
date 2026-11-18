import json 
import anthropic 

def synthesize_insights(topic, 
                        articles,
                        benchmark,
                        compliance_risks):

    client  = anthropic.Anthropic()

    prompt = f"""
       Combine both sources into a clean, strictly organized data structure. 
       {topic} is the topic of interest.
       use only data given. DO not invent
       News: {articles}
       Benchmarks: {benchmark}
       Compliance Risks: {compliance_risks}
         """

    reply = client.messages.create(
        model="claude-3.0",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ])
    try:
        data = json.loads(reply)
    except json.JSONDecodeError:
        print("Failed to parse the response as JSON.")
        data = None
    return data