class Taxi( Transportation ):

   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      return self.distance*40
