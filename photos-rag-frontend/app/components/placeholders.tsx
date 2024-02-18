import { useState, useEffect } from 'react';

function useDynamicPlaceholder(
  listOfPlaceholders: string[],
  typingSpeed: number = 25, // This value controls both typing and deleting speed
  pauseDuration: number = 1000 // Duration to pause after typing before deleting
): string {
  const [placeholder, setPlaceholder] = useState('');
  const [index, setIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [reverse, setReverse] = useState(false);

  useEffect(() => {
    // Start reversing (deleting) immediately after the full text is typed
    if (!reverse && charIndex === listOfPlaceholders[index].length) {
      // Pause before starting to delete
      setTimeout(() => setReverse(true), pauseDuration);
      return;
    }

    // Switch to the next placeholder after the current text is fully deleted
    if (reverse && charIndex === 0) {
      setReverse(false);
      setIndex((prevIndex) => (prevIndex + 1) % listOfPlaceholders.length);
      return;
    }

    // Schedule the next update
    const timeout = setTimeout(() => {
      setPlaceholder((prev) =>
        reverse ? prev.substring(0, prev.length - 1) : prev + listOfPlaceholders[index][charIndex]
      );
      setCharIndex(reverse ? charIndex - 1 : charIndex + 1);
    }, typingSpeed); // Use the same speed for both typing and deleting

    return () => clearTimeout(timeout);
  }, [charIndex, index, reverse, listOfPlaceholders, typingSpeed, pauseDuration]);

  return placeholder;
}

export default useDynamicPlaceholder;
