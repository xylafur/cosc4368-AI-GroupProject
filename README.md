All of the source code is located in the 'src' directory.

Everything is as contained as possible, meaning every module tries to not use
anything from any other module unless it absolutley has to.  Modules in the src
directory either construct objects that represent entities in the experiment or
functions that manipulate those entities and run using information contained
within them.

For example the 'Agent' object in agent.py has all of the information that the
agent would contain such as its current position as an x, y point and wether or
not it is holding a block

The 'World' object in world.py contains everything about the world, which
really is just a grid of 'Location' objects.  Some of these 'Location' objects
are pick up and drop offs, others are not.  Other than that the World object
has the behavior of the world defined as functions.

These two object know nothing about eachother.  All of the functions in World
can be implemented without an Agent object.  All of the functions in Agent can
be implemented without a World object.  The World does not know the position of
the Agent, only the Agent knows his position (as an x, y point).

For certain modules though it does make sense to take in another object as a
parameter.  For example, the q learning functions.  In the q learning functions
you need to determine all of the valid actions that the agent can take.  The
World module has a function that will take in a given position and return a
list of valid actions that could be taken.  Thus it makes sense for those
functions to take in the world object.  Additionally those functions could also
take in either the agent object (from which the x, y position can be obtained)
or the raw x, y position of the agent.

It is also worth noting in the previous example that neither world nor agent
would have to be imported into the q learning module.  The objects can be
passed into the function be some other higher level mechanism (such as the
manager) that has imported the agent.  In python, You do not need to import an
object to use it if it has been passed into your function as a parameter.


The intended purpose behind each of the modules is such:
    location.py
        Has the definitions for the objects that represent individual squares
        (locations) in the world.  There are 3 object types that are used by
        the rest of the modules (4 in total).  Pick up locations, drop off
        locations and then normal locations which are neither.

        The only module that should need this one, is the world module.

        Each of these location objects has various functions that allow the
        user to get the reward associated with that location, get the type and
        possibly pick up and drop off blocks (depending on the type).


    world.py
        Has the definition of the actual world.  The world is just made up of a
        grid of locations.

        The world does not keep track of the position of the agent!

        The world should not change!  The only thing that will change about the
        world is blocks will be picked up from pick up locations and dropped
        off onto the drop off locations.  Thus only a few of the locations in
        the grid that makes up the world will change.

        This world object allows the user to easily grab particular squares
        from the grid and determine the type of location they are.  It also
        allows the user to pick up and drop off block from those locations with
        ease.

        There are also other various helper functions

        NOTE:
            The agent is not stored in the world! It is up to some higher level
            mechanism to determine where in the world the agent is.

            I made this design decision, because if the agent is a part of the
            world, there are too many ambigious questions.  Does the world own
            the agent, or does the agent own the world?  If the answer is both,
            then who holds the information about the position of the agent?
            Both?  Then we have to update both objects each time the agent
            moves.

    agent.py
        Has the definition of the Agent object. The Agent object represents out
        agent that goes around picking up and dropping off blocks.

        The agent keeps track of his position in the world as an x y position,
        and exposes the user functions that allow him to move either north,
        south, east or west as well as pick up and drop off blocks

    qtable.py
        Has the definition for the qtable that will store all of our data.

        Allows the user easy access to all of the information stored inside it

    functions.py
        This contains all of the qlearning functions!

        Both q learning and SARSA should be implemented as functions that take
        in the same parameters.  This way, we can have one single wrapper
        function that can call either of these functions based on parameters.
        This way our design is extremley modular, we would only have to change
        input parameters to the wrapper function and that should allow all of
        the experiments to be ran.

    manager.py
        This modules contains the wrapper function that was mentioned in the
        functions.py module definition.  This function should be able to run
        all of the experiments that we are supposed to compute by just chaning
        parameters.

        Because of the abstractions provided by all of the other modules, it
        should be relatively easy to make this function generic and well
        organized.

    main.py
        This module parses command line arguments and then envokes the manager
        function after constructing the table and agent objects.

