class Handler:
    def __init__(self, callback, event_type=None):
        self.event_type = event_type
        self.callback = callback
        
    def __call__(self, event, context):
        if self.event_type is None or event.type == self.event_type:
            return self.callback(event, context)
        
