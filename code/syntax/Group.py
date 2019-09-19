class Group:
    
    Group world
    leadId = 0
    mask = 0
    procs = None
    isLocal = false
    procTree = None

    def __init__(self, procs, leadId, mask, isLocal, world):
        self.procs = procs
        self.leadId = leadId
        self.mask = mask
        self.isLocal = isLocal
        self.world = world

    def getProcs(self):
        return self.procs

    def getDims(self):
        return self.mask

    def isMember(self):
        return self.isLocal

    def isLead(self):
        return self.procs.id() == leadId


