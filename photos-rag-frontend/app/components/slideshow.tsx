// components/slideshow.tsx
import React, { useState } from 'react';
import '../styles/slideshow.css';

// Define an interface for the prop structure
interface ResultItem {
    caption: string;
    signed_url: string;
  }
  
interface PhotoSlideshowProps {
    results: ResultItem[];
  }

const PhotoSlideshow: React.FC<PhotoSlideshowProps> = ({ results }) => {
  const [currentIndex, setCurrentIndex] = useState(0);

  const nextSlide = () => {
    setCurrentIndex((currentIndex + 1) % results.length); // Cycle forward
  };

  const prevSlide = () => {
    const newIndex = currentIndex - 1 < 0 ? results.length - 1 : currentIndex - 1;
    setCurrentIndex(newIndex); // Cycle backward
  };

  if (!Array.isArray(results) || results.length <= 0) {
    return null; // or some placeholder content
  }

  return (
    <div className="slideshow-container">
        <div className="image-container">
            {results.map((result, index) => (
                <div className={index === currentIndex ? 'slide active' : 'slide'} key={result.signed_url}> {/* Use signed_url as key */}
                    {index === currentIndex && (
                        <img src={result.signed_url} alt="Slide" className="image" />
                    )}
                </div>
            ))}
        </div>
        <div className="controls">
            <button className="prev" onClick={prevSlide}>&#10094;</button>
            <button className="next" onClick={nextSlide}>&#10095;</button>
        </div>
        {/* Display the caption of the currently active slide */}
        {results.length > 0 && (
            <div className="caption">{results[currentIndex].caption}</div>
        )}
    </div>
    );
};

export default PhotoSlideshow;
