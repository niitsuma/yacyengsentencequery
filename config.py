# --- Configuration for YaCyBot ---
# vim: ts=2 sw=2 expandtab

# ----------------------------------------------------------------------------
# "THE PIZZA-WARE LICENSE" (derived from "THE BEER-WARE LICENCE"):
# <cfr34k-yacy@tkolb.de> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a pizza in return. - Thomas Kolb
# ----------------------------------------------------------------------------

IRC_SERVER  = "localhost" # Hostname / IP of the IRC server
IRC_PORT    = 61234       # Port of the IRC server
IRC_NICK    = "YaCyBot"   # Nick of the bot

# A list of channels that should be joined. The bot will be available in all
# channels simultaneously.
IRC_CHANNELS = [
  "#yacytest"
  ]

# Increase this if the server drops messages because of flood protection
IRC_MIN_DELAY = 0.8

# If this is not zero, a /ping command is sent to the server every
# IRC_PING_INTERVAL seconds
IRC_PING_INTERVAL = 300

YACY_ADDRESS     = "localhost" # Hostname / IP of the YaCy-Peer
YACY_PORT        = 8091        # Port of the YaCy-Peer

# Default parameters for the request URL
#http://localhost:8091/solr/select?hl=false&wt=yjson&facet=true&facet.mincount=1&facet.field=url_file_ext_s&start=0&rows=10&query=www
YACY_DEFAULT_PARAMS = {
    #,
    #'rows' :  "3" 
  }
# 'wt' : "yjson"
#    'hl' : "false",
#    'facet' : "true",
#    'facet.mincount' : "1" , 
#    'facet.field' : "url_file_ext_s",
#    'start' : "0",

#'wt':'yjson'

# How often statistics are actually reloaded from the peer (in seconds)
YACY_STATS_UPDATE_INTERVAL = 60

# The timeout passed to urllib2.urlopen.
# Decrease this value if the Bot is frequently disconnected by the IRC Server
# when the YaCy peer is hanging
URLLIB_TIMEOUT = 60

OUTPUT_DIR = "/home/niitsumalocal/tmp/"
