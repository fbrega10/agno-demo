from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.hackernews import HackerNewsTools
from agno.tools.wikipedia import WikipediaTools
from agno.db.sqlite import SqliteDb


#Tools definition
def classify_topic(title: str) -> str:
  title = title.lower()

  topics = {
      'ai' : ['ai', 'llm', 'gpt', 'model', 'neural', 'transformer'],
      'web' : ['web', 'browser', 'css', 'javascript', 'react'],
      'security': ['security', 'hack', 'vulnerability', 'cve', 'encrypt'],
      'business': ['startup', 'funding', 'acquisition', 'ipo', 'revenue'],
      'hardware': ['chip', 'gpu', 'hardware', 'risc', 'arm']
      }
    
  final_topic = 'other'
  for topic in list(topics.keys()):
      arg_list = topics.get(topic)
      if any(arg_list.count(c) > 0 for c in title.split()):
        return topic
  return final_topic

agent = Agent(
    model=MistralChat('mistral-small-latest'),
    instructions=[ "Sei un analista tech. Scrivi sempre in italiano.",
     "Usa get_top_hackernews_stories per le notizie.",
     "Usa classify_topic per classificare ogni titolo.",
     "Usa search_wikipedia per approfondire un argomento."],
      tools=[HackerNewsTools().get_top_hackernews_stories, classify_topic, WikipediaTools()],
      db=SqliteDb('tmp/agno_demo.db'),
      markdown=True,
      num_history_messages=5,
      add_history_to_context=True
)



#Test agent response

agent.print_response(
    "Recupera le top 3 story da Hacker News, classifica ciascuna per categoria, "
    "poi cerca su Wikipedia il tema della prima story e scrivi un bollettino tech in italiano.",
    stream=True
)
