import requests

from pyrogram import Filters, Message

from rosebot import BOT
from rosebot.helpers import ReplyCheck


query = """
query get_data($substance_name: String) {
  substances(query: $substance_name) {
    name
    url
    effects {
        name
        url
    }
    class {
      psychoactive
      chemical
    }
    dangerousInteractions {
      name
      url
    }
    unsafeInteractions {
      name
      url
    }
    uncertainInteractions{
      name
      url
    }
    addictionPotential
    roas {
      name
    }
    roa {
      oral {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      sublingual {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      buccal {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      insufflated {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      rectal {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      transdermal {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      subcutaneous {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      intramuscular {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      intravenous {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
      smoked {
        name
        duration {
          comeup {
            min
            max
            units
          }
          onset {
            min
            max
            units
          }
          peak {
            min
            max
            units
          }
          offset {
            min
            max
            units
          }
          afterglow {
            min
            max
            units
          }
          total {
            min
            max
            units
          }
          duration {
            min
            max
            units
          }
        }
        dose {
          threshold
          light {
            min
            max
          }
          common {
            min
            max
          }
          strong {
            min
            max
          }
          heavy
          units
        }
      }
    }
  }
}
"""


def get_data_from_api(substance):
    r = requests.post(
        "https://api.psychonautwiki.org/",
        json={"query": query, "variables": {"substance_name": substance}},
    )
    if r.status_code == 200:
        data = r.json()
        return data


def text_effects(data):
    effects = "**Effects**"
    for effect in data["data"]["substances"][0]["effects"]:
        effects = "{}\n[{}]({})".format(effects, effect["name"], effect["url"])
    return effects


def dangerous_interactions(data):
    dangerousinteractions_list = ""
    try:
        for interaction in data["data"]["substances"][0]["dangerousInteractions"]:
            dangerousinteractions_list = "{}\n[{}]({})".format(
                dangerousinteractions_list, interaction["name"], interaction["url"]
            )
    except TypeError:
        pass
    try:
        for interaction in data["data"]["substances"][0]["unsafeInteractions"]:
            dangerousinteractions_list = "{}\n[{}]({})".format(
                dangerousinteractions_list, interaction["name"], interaction["url"]
            )
    except TypeError:
        pass
    try:
        for interaction in data["data"]["substances"][0]["uncertainInteractions"]:
            dangerousinteractions_list = "{}\n[{}]({})".format(
                dangerousinteractions_list, interaction["name"], interaction["url"]
            )
    except TypeError:
        pass
    return dangerousinteractions_list


def dosing_data(data):
    roa = data["data"]["substances"][0]["roas"][0]["name"]
    dosingdata = data["data"]["substances"][0]["roa"][roa]
    units = dosingdata["dose"]["units"]
    if dosingdata["dose"]["threshold"] is not None:
        threshold = "Threshold: {} {}\n".format(dosingdata["dose"]["threshold"], units)
    else:
        threshold = ""
    light = "Light: {} - {} {}\n".format(
        dosingdata["dose"]["light"]["min"], dosingdata["dose"]["light"]["max"], units
    )
    common = "Common: {} - {} {}\n".format(
        dosingdata["dose"]["common"]["min"], dosingdata["dose"]["common"]["max"], units
    )
    strong = "Strong: {} - {} {}\n".format(
        dosingdata["dose"]["strong"]["min"], dosingdata["dose"]["strong"]["max"], units
    )
    if dosingdata["dose"]["heavy"] is not None:
        heavy = "Heavy: {} {}\n".format(dosingdata["dose"]["heavy"], units)
    else:
        heavy = ""
    dosage = "\nRoute of administration: **{}**\n{}{}{}{}{}".format(
        roa, threshold, light, common, strong, heavy
    )
    return dosage


def duration_data(data):
    roa = data["data"]["substances"][0]["roas"][0]["name"]
    dosingdata = data["data"]["substances"][0]["roa"][roa]
    total = ""
    comeup = ""
    onset = ""
    offset = ""
    peak = ""
    afterglow = ""
    try:
        total = "Total: {} - {} {}\n".format(
            dosingdata["duration"]["total"]["min"],
            dosingdata["duration"]["total"]["max"],
            dosingdata["duration"]["total"]["units"],
        )
    except TypeError:
        comeup = ""
    try:
        onset = "Onset: {} - {} {}\n".format(
            dosingdata["duration"]["onset"]["min"],
            dosingdata["duration"]["onset"]["max"],
            dosingdata["duration"]["onset"]["units"],
        )
    except TypeError:
        comeup = ""
    try:
        comeup = "Comeup: {} - {} {}\n".format(
            dosingdata["duration"]["comeup"]["min"],
            dosingdata["duration"]["comeup"]["max"],
            dosingdata["duration"]["comeup"]["units"],
        )
    except TypeError:
        comeup = ""
    try:
        peak = "Peak: {} - {} {}\n".format(
            dosingdata["duration"]["peak"]["min"],
            dosingdata["duration"]["peak"]["max"],
            dosingdata["duration"]["peak"]["units"],
        )
    except TypeError:
        comeup = ""
    try:
        offset = "Offset: {} - {} {}\n".format(
            dosingdata["duration"]["offset"]["min"],
            dosingdata["duration"]["offset"]["max"],
            dosingdata["duration"]["offset"]["units"],
        )
    except TypeError:
        comeup = ""
    try:
        afterglow = "Afterglow: {} - {} {}\n".format(
            dosingdata["duration"]["afterglow"]["min"],
            dosingdata["duration"]["afterglow"]["max"],
            dosingdata["duration"]["afterglow"]["units"],
        )
    except TypeError:
        comeup = ""
    duration = "\n{}{}{}{}{}{}".format(total, onset, comeup, peak, offset, afterglow)
    return duration


def summary(data):
    substance_name = "**Name:** [{}]({})\n".format(
        data["data"]["substances"][0]["name"], data["data"]["substances"][0]["url"]
    )
    s_name = data["data"]["substances"][0]["name"]
    try:
        psychoactive_class = "**Psychoactive class:** {}\n".format(
            data["data"]["substances"][0]["class"]["psychoactive"][0]
        )
    except TypeError:
        psychoactive_class = ""
    try:
        chemical_class = "**Chemical class:** {}\n".format(
            data["data"]["substances"][0]["class"]["chemical"][0]
        )
    except TypeError:
        chemical_class = ""
    try:
        addiction_potential = "**Addiction potential:** {}\n".format(
            data["data"]["substances"][0]["addictionPotential"]
        )
    except TypeError:
        addiction_potential = ""
    dosages = "\n**Dosage:** {}\n".format(dosing_data(data))
    duration = "**Duration:** {}\n".format(duration_data(data))
    dangerous_interactions_list = dangerous_interactions(data)
    wp_summary = "**Wikipedia Summary:**\n{}\n\n".format(wikipedia_summary(s_name))
    print(wp_summary)
    if dangerous_interactions_list is not "":
        interactions = "**Dangerous interactions:** {}\n".format(
            dangerous_interactions_list
        )
    else:
        interactions = ""
    text = "{}{}{}{}{}{}{}{}".format(
        substance_name,
        psychoactive_class,
        chemical_class,
        addiction_potential,
        dosages,
        duration,
        wp_summary,
        interactions,
    )
    return text


def get_drug(substance):
    data = get_data_from_api(substance)
    if not data["data"]["substances"]:
        return
    else:
        text = summary(data)
        effects = text_effects(data)
        return text, effects


def wikipedia_summary(topic):
    r = requests.get(
        "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(topic)
    )
    if r.status_code == 200:
        data = r.json()
        text = "{}\n**Read more at:** [{}]({})".format(
            data["extract"], data["title"], data["content_urls"]["desktop"]["page"]
        )
        return text


@BOT.on_message(Filters.command("pwiki", "!"))
def pwiki(bot: BOT, message: Message):
    drug = message.text.replace("!pwiki ", "")
    text = get_drug(drug)
    BOT.send_message(
        chat_id=message.chat.id,
        text=text[0],
        disable_notification=True,
        reply_to_message_id=ReplyCheck(message),
    )
    BOT.send_message(
        chat_id=message.chat.id,
        text=text[1],
        disable_notification=True
    )
    if message.from_user.is_self:
        message.delete()
