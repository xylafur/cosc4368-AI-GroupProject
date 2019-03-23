All of the source code is located in the 'src' directory.

Everything is as contained as possible, meaning every module tries to not use
anything from any other module unless it absolutley has to.  Modules in the src
directory either construct objects that represent entities in the experiment or
functions that manipulate those entities and run using information contained
within them.

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

    agent.py
        Has the definition of the Agent object. The Agent object represents out
        agent that goes around picking up and dropping off blocks.
        The agent keeps track of his position in the world, and exposes the
        user functions that allow him to move either north, south, east or west
        as well as pick up and drop off blocks

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

