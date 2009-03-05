###
# Copyright (c) 2007, Brad Anderson
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import random
import re
import urllib
import BeautifulSoup

class Lolz(callbacks.PluginRegexp):
    """Just lol."""
    regexps = ['lolzSnarfer', 'brbSnarfer', 'rightTeslaSnarfer', 'dreamSnarfer', 'upYoursSnarfer', 'meAndMyXSnarfer', 'hillarySnarfer', 'fuckYouSnarfer', 'suchADickSnarfer', 'dayManSnarfer', 'masterOfKarateSnarfer', 'calculatorSnarfer', 'dagSnarfer', 'letTheRecordSnarfer', 'failSnarfer', 'urlTitleSnarfer']

    def lolz(self, irc, msg, args):
    	"""lolz"""
        irc.reply("lolz")

    def sentence(self, irc, msg, args):
    	"""sentence users for infractions of decency"""
        channel = msg.args[0]
        if not irc.isChannel(channel):
	        return
        if "freerice" in [ arg.lower() for arg in args[2:] ]:
		    irc.reply("%s: You have been sentenced to earn %s grains on FreeRice <http://www.freerice.com/index.php?&s=English%%20Grammar>" % (args[0], args[2]), prefixNick=False)
        if set(["esr's", "questions"]).issubset(set([ arg.lower() for arg in args[2:] ])):
		    irc.reply("%s: You have been sentenced to read ESR's Asking Smart Questions <http://www.catb.org/~esr/faqs/smart-questions.html>" % (args[0]), prefixNick=False)

    def lolzSnarfer(self, irc, msg, match):
    	r"[ ]+lol[ ]*|[ ]*lol[ ]+|^lol$|^ehl oh ehl$"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        irc.reply("lolz", prefixNick=False)

    def brbSnarfer(self, irc, msg, match):
        r"([ ]+|^)brb[.!]*$"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        irc.reply("Good riddance.", prefixNick=False)

    def rightTeslaSnarfer(self, irc, msg, match):
        r"right[,]* tesla[?]*|isn[']*t it[,]* tesla[?]*"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        irc.reply("True dat.", prefixNick=False)

    def dreamSnarfer(self, irc, msg, match):
    	r"i had this dream |i had a dream | dream i had"
    	channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        irc.reply("I had a dream where a hamburger was eating ME!", prefixNick=False)

    def upYoursSnarfer(self, irc, msg, match):
    	r"isn't it a lovely mornin[g']"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        irc.reply("Up yours, nigger!", prefixNick=False)

    def meAndMyXSnarfer(self, irc, msg, match):
    	r"me and (my|your|his|her|its|our|their|whose) (\w+)"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        irc.reply("%s %s and I!" % (match.group(1).capitalize(), match.group(2)), prefixNick=False)

    def hillarySnarfer(self, irc, msg, match):
    	r"[ ]+hillary[ ]*|[ ]*hillary[ ]+|^hillary$"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        if random() > 0.25:
            return
        irc.reply("Don't let the door hit your ass on the way out, Hillary.  Leave that to Bill.", prefixNick=False)

    def fuckYouSnarfer(self, irc, msg, match):
    	r"fuck you, tesla|fuck you tesla"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("Fuck me?! FUCK YOU!", prefixNick=True)

    def suchADickSnarfer(self, irc, msg, match):
    	r"you( are|[']re) such a (dick|jerk|ass)[, ]+tesla"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("Heh... yeah.", prefixNick=False)

    def dayManSnarfer(self, irc, msg, match):
    	r"^day[ ]*man[!]*|^fighter of the night[ ]*man[!]*|^champion of the sun[!]*"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("UuuwaaAAaaaAAAaaa!", prefixNick=False)

    def masterOfKarateSnarfer(self, irc, msg, match):
    	r"^you're a master of karate[!]*"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("...and friendship!", prefixNick=False)
        irc.reply("For everyone!", prefixNick=False)

    def calculatorSnarfer(self, irc, msg, match):
    	r"what('s| is) [0-9]+[ ]*[+\-*/][ ]*([0-9]+|the number of horns a unicorn has)[ =?]*"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("Calculating...", prefixNick=True)
        irc.reply("...", prefixNick=False)
        irc.reply("Answer: Your mom.", prefixNick=False)

    def dagSnarfer(self, irc, msg, match):
    	r"^dag| dag[!?]*$| dag |david alan grier"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("Don't. Look at. Me!", prefixNick=False)
        irc.reply("I will. Give. You. Somethin... to smile... about...", prefixNick=False)
        irc.reply("huh oh oh oh huh ah huh huh huhuhohohohohOOH!", prefixNick=False)
        irc.reply("*zzzzz*", prefixNick=False)

    def letTheRecordSnarfer(self, irc, msg, match):
    	r"^Let the record show that "
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("The record has been updated.", prefixNick=False)

    def failSnarfer(self, irc, msg, match):
    	r"^ /win [0-9]+$|^win [0-9]+$"
	    channel = msg.args[0]
        if not irc.isChannel(channel):
            return

        irc.reply("FAIL", prefixNick=False)
        
    def urlTitleSnarfer(self, irc, msg, match):
        r"https?://([-\w\.]+)+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        
        try:
            url = urllib.urlopen(match.group())
        except IOError:
            return
            
        title = BeautifulSoup.BeautifulSoup(url).title.string
        
        irc.reply("[ %s ]" % (title,), prefixNick=False)
        
Class = Lolz


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
