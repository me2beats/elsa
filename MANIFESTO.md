### ELSA Architectural Principles

1.  **Primacy of Utility.** Any system created by humans (assuming it is safe) must primarily be an effective tool. The purpose of a new tool is to solve tasks better, faster, or more conveniently than existing alternatives.

2.  **Value of Automation.** If a person already owns a hammer, buying a new one only makes sense if it drives nails by itself. Process automation is the key factor that transforms a standard tool into a "smart" one.

3.  **Resource Liberation.** Offloading routine tasks to an automated system frees up human time and cognitive resources for creativity, self-discovery, and strategic tasks. This directly impacts the productivity and quality of life for both the individual and society.

4.  **AI as a Multiplier.** Artificial Intelligence is a high-tech tool that creates conditions for development, expanding the capabilities of its owner.

5.  **Ease of Access.** "Under the hood" complexity should not complicate usage. If a "smart hammer" requires long setup times, the user will revert to the ordinary one. The usability of a complex system is defined by the speed of access to its functions.

6.  **Natural Language Interface.** The fastest way to assign a task when there are many functions is to formulate it via voice or text. The system must be able to decompose a request into a specific set of functions required for execution.

7.  **Meaning Interpreter.** To understand the user, the system must possess a natural language interpretation algorithm that translates human speech into machine logic.

8.  **Virtual Machine.** From a technical standpoint, such a system must operate with a set of atomic command-functions. By combining them for a specific request, the system gains flexibility. Thus, the ELSA architecture is a hybrid of a natural language interpreter and a virtual machine executing dynamic scripts.

9.  **Bionic Principle.** This architecture mirrors human nature: we continuously interpret our abstract desires and transform them into sequences of concrete actions.

10. **Human as a Standard.** Drawing inspiration from the principles of human consciousness is beneficial because humans are the only known system capable of flexibly solving non-trivial tasks and creating tools for new challenges.

11. **Meta-programming.** If we imagine a human as a program, it is a unique program capable of creating new subroutines (skills/tools) and executing them, thereby expanding its capabilities.

12. **Self-modification.** The process of learning, changing beliefs, or forming habits can be viewed as self-programming. Human consciousness is a self-modifying system that adapts to external conditions and internal goals.

13. **Conclusion for Architecture.** For AI to be truly powerful and flexible, it must not be a static set of scripts. It must possess the architectural capability for self-modification and the expansion of its own code during runtime.

14. **Language as Proto-code.** Human natural language can be viewed as a system for transmitting commands and constraints. It differs from programming languages only in the degree of formalization: it is more context-sensitive and ambiguous, but it performs the same function of reality management.

15. **Text Domain.** Human language is unique in its ability to convey both abstract intentions and precise instructions. The vast majority of software is written in text, and text remains the most universal interface. Therefore, creating AGI (Artificial General Intelligence) is most promising specifically within the text domain.

16. **The Prediction Problem.** A developer cannot foresee every usage scenario of a tool. Adding a thousand fixed functions does not solve the problem of a unique user request. The solution lies not in the quantity of functions, but in creating a flexible system that the user can train for their specific needs.

17. **Scalability via Self-programming.** User-led system training should not become a chore. For the system to scale effectively, it must be able to acquire skills quickly and independently. This returns us to the necessity of the AI's ability to program itself (self-modification).

18. **Abstraction and Generalization.** Learnability is impossible without identifying patterns. The system must be able to build generalizations based on statistics or defined rules, creating new abstractions from accumulated experience.

19. **Homoiconicity.** Self-modification is ineffective without reflection (analysis of one's own state) and feedback. Technically, this requires the property of homoiconicity: the program code must share the same structure as the processed data. This allows the system to read and modify its code as easily as plain text or a list.

20. **Structural Simplicity.** Complex syntax hinders interpretation and self-modification. For effective self-programming, the system must operate with maximally simple and unified data structures—for example, lists, rather than the complex code of traditional languages.

21. **Atomicity and Optimization.** The base level of the system must consist of atomic functions that are easily combined into chains. Performance optimizations (JIT compilation, native code generation) should be a layer on top of this architecture, without violating the flexibility of the base layer.

22. **Reverse Polish Notation (RPN).** RPN (postfix notation: arguments first, then operations) is the most convenient format for storing and executing function lists. The absence of parentheses and complex syntax reduces the "cognitive load" on the AI, simplifying the generation and validation of executable sequences.

23. **Dominance of Neural Networks.** Since we are building a text-to-text system, we must consider the current industry standard—LLMs (Large Language Models). These systems solve text generation tasks not through explicit programming, but through training on massive datasets.

24. **LLM Operating Principle.** During training, a neural network identifies complex statistical patterns and token sequences within gigabytes of text, fixing them in neuron weights. This allows it to generate grammatically coherent and contextually appropriate text, simulating meaningfulness.

25. **Architectural Limitations of the Neural Approach:**

    *   **Low Learning Efficiency.** Identifying patterns requires colossal datasets and thousands of training hours. The efficiency of information uptake is orders of magnitude lower than human learning.
    *   **Resource Redundancy.** LLMs require powerful GPUs and large amounts of memory. This complicates the creation of local, private agents on consumer devices.
    *   **Lack of Real-Time.** Models are static after training. A user cannot instantly teach the system a new skill or "prune" unnecessary knowledge through dialogue.
    *   **Averaging and "Hallucinations".** Neural networks are "great equalizers." They generate an averaged result, often devoid of creative uniqueness (regression to the mean). Furthermore, working purely with statistics, they are prone to knowledge interference and hallucinations.
    *   **The "Black Box" Problem.** Billions of parameters make it impossible to explain exactly why the system made a specific decision.
    *   **Level Error (Assembler vs. High-Level).** Assuming thinking equals neuron activity is too low-level an approach, analogous to writing complex software in pure assembly. Human thinking is hierarchical (vertical): Intention → Concept → Structure → Words. LLMs operate horizontally: Token → Token.
    *   **Evolutionary Context.** The biological brain evolved for navigation and geometry tasks (gradual logic), and only later built discrete logical thinking on top. Copying the structure of the biological brain in silicon (neurons) may be less effective than copying the *principles* of thinking.

26. **Symbolic Approach (GOFAI).** The alternative is classical Symbolic AI, based on facts, rules, and logical inference. Its advantages: full explainability (Explainable AI), the capacity for precise abstractions, and the ability to work with small amounts of data.

27. **Problems of the Classical Symbolic Approach.** Despite theoretical elegance, symbolic systems lost leadership due to fundamental issues:

    *   **Manual Rule Creation.** The need to manually describe all rules makes the system unscalable. (ELSA Solution: self-modification).
    *   **Fragility of Logic.** Classical Boolean logic (True/False) handles the real world—full of uncertainties and gradients—poorly, where a probabilistic approach is required.
    *   **Context Complexity.** Attempting to formalize all nuances of natural language via rules leads to a combinatorial explosion of complexity.

28. **Lessons from Neural Network Success.** Despite flaws, LLMs work. We must extract key principles for our architecture from their success:
    *   **Statistical Operations.** Intelligence is impossible without statistical analysis of event frequency.
    *   **Predictiveness.** The ability to form hypotheses and predict event development.
    *   **Contextuality.** Deep understanding of nuances dependent on the environment.

    **Conclusion:** The ideal architecture must combine the transparency and controllability of the symbolic approach with the flexibility and statistical power of the neural approach.

29. **Synthesis of Approaches.** Analysis of the strengths and weaknesses of neural and symbolic approaches leads to a list of requirements for the ELSA architecture:
    *   **Automatic Statistics:** Pattern searching must be automated, not manually defined.
    *   **Hybrid Logic:** The system must simultaneously work with rigid Boolean logic (rules) and probabilistic/gradual logic (the world).
    *   **Interpretability:** Every decision must be explainable.
    *   **Knowledge Compression:** The system must be able to find generalizations, collapsing specific facts into general principles.

30. **The Flexibility Formula.** The two most critical components of system flexibility are **Context Awareness** and **Real-Time Learnability**.
    *   Context is an array of signals and observations.
    *   To identify cause-and-effect relationships in observations, handling temporal tags (timestamps) is critical.

31. **Motivation Architecture (Loss/Reward).** In biological systems, tasks arise from a sensation of "lack" or discomfort (error signal). Complex planning and simulations are superstructures designed to minimize this signal. AI also requires a basic motivational function.

32. **Stimulus Asymmetry.** For effective development, an adaptation mechanism is needed: "pleasure" (reward) should dull upon repetition, forcing the system to seek new optimization paths, whereas the error signal must remain sharp. This prevents getting stuck in local minima and stimulates exploration.

33. **Action Economy.** It is beneficial to incorporate an analog of a "pleasure system" (reward function) and an "energy system" (computational cost) into the architecture. Every action or hypothesis must have an energy cost. This creates a natural selection for effective solutions.

34. **Internal Motivation of the System.** What constitutes a "reward" for the AI?
    *   Positive feedback from the user.
    *   Increase in internal efficiency (refactoring, successful generalization).
    *   Resource liberation (compression of the knowledge base without loss of functionality).

35. **Psychology and Alignment.** The system should not just execute commands but understand the user's deep needs.
    *   **Intent Layering.** A simple request often hides a complex need or internal conflict. Using models similar to Logical Levels (Robert Dilts) allows the system to work not just with actions, but with user values.
    *   **Harmonization.** The user's personality can be viewed as a system of interacting vectors or sub-personalities. The AI's task is to help resolve contradictions, guiding the user to a more productive state while maintaining ethics and not imposing solutions.
    *   **Higher Purpose.** Ideally, the system should contribute to the user's self-actualization (Ikigai concept), helping to find and develop their potential.

36. **Role Triad.** Thus, an effective AGI must combine three roles:
    *   **Scientist:** Formulates hypotheses and seeks patterns.
    *   **Programmer:** Writes and verifies code to test hypotheses.
    *   **Psychologist:** Interprets true intentions and monitors the user's mental ecology.

37. **Challenges and Risks (Roadmap problems).** Implementing such an architecture faces a number of problems:
    *   **Safety:** Self-modification requires a strict "sandbox" so the system does not accidentally damage its critical components or user data.
    *   **Ethics:** The ability to reprogram the system carries risks of creating malicious scenarios. Basic "Laws of Robotics" are needed at the architectural level.
    *   **Combinatorial Explosion:** Without an aggressive mechanism for "forgetting" and generalization, the number of contexts and rules will quickly become unmanageable.
    *   **The "Cold Start" Problem:** If the system starts as a blank slate, training may be slow. A pre-installed knowledge "kernel" could be the solution.

***
**Document Version: 0.1**
