import sys
import pinder
from trac.core import *
from trac.ticket.api import ITicketChangeListener

class CampfireListener(Component):
    implements(ITicketChangeListener)

    def _sendText(self, ticketid, text):
        try:
            c = pinder.Campfire('SUBDOMAIN', 'API TOKEN')
            room = c.room('ROOM ID')
            room.speak("Trac: ticket #%i (http://trac.YOURDOMAIN.com/projects/PROJECT/ticket/%i) %s" % (ticketid, ticketid, text))

        except:
            print "Unexpected error:", sys.exc_info()[0]
            return

    def ticket_created(self, ticket):
        self._sendText(ticket.id, "\"%s\" created by %s." % (ticket.values['summary'][0:100], ticket.values['reporter']))

    def ticket_changed(self, ticket, comment, author, old_values):
        self._sendText(ticket.id, "changed by %s, Comment: %s." % (author, comment[0:100]))

    def ticket_deleted(self, ticket):
        self._sendText(ticket.id, "Ticket deleted")

