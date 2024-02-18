// app/page.tsx
'use client'
import { useState } from 'react';
import Head from 'next/head';
import './styles/page.css';
import useDynamicPlaceholder from './components/placeholders';
import PhotoSlideshow from './components/slideshow'; // Ensure this import is correct

interface ResultItem {
  caption: string;
  signed_url: string;
}

export default function Page() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<ResultItem[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const dynamicPlaceholder = useDynamicPlaceholder([
    "Daniel, Santiago, Kika, and Pipe wearing Michigan gear",
    "Daniel enjoying beers with Azul, Javier, Julio, Will, and Pablo in Ann Arbor",
    "Daniel, Santiago, Juan, Graciela, and Pipe hiking in Mount Rainier",
    "Daniel and Sri celebrating a Duke Football win"
  ], 25, 1000); // Adjust typing speed and pause duration as needed

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsLoading(true); // Start loading
    try {
        const response = await fetch('http://127.0.0.1:5000/get_images', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });

        if (response.ok) {
          const rawData = await response.json();
          // Assuming all relevant data is under a 'response' key or similar
          const data = rawData.response; // Adjust this line based on the actual key used in your backend response
      
          const formattedResults = Object.entries(data).map(([signed_url, caption]) => ({
              signed_url, // signed_url is already a string, no need for assertion
              caption: caption as string // Asserting caption as string is correct
          }));
          // Reverse the order of formatted results
          const reverseFormattedResults = formattedResults.reverse();
          // Preload images
          reverseFormattedResults.forEach(({ signed_url }) => {
            const img = new Image(); // Create a new Image object
            img.src = signed_url; // Set the source of the image to the signed URL
          });
          console.log('Results:', reverseFormattedResults);
          setResults(reverseFormattedResults);
        } else {
            console.error('Failed to fetch results');
        }
    } catch (error) {
        console.error('Error:', error);
    } finally {
        setIsLoading(false); // Stop loading
    }

};

  return (
    <>
      <Head>
        <title>Daniel&apos;s Life</title>
      </Head>
      <div className="container">
        <h1 className="title">Daniel&apos;s Life</h1>
        <p>Welcome to Daniel&apos;s Life, a website where you can query highlights of Daniel&apos;s favorite moments involving his friends and family. Currently, you can browse moments from the years 2022 and 2023.</p>
        <form onSubmit={handleSubmit} className="input-container">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={dynamicPlaceholder}
            className="input"
          />
          <button type="submit" className="button">Submit</button>
        </form>
        {isLoading ? (
          <div className="loading-container" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
            <div className="loading-spinner" style={{ marginBottom: '10px' }}></div> {/* Or any other loading indicator */}
            <p style={{ margin: 0 }}>Fetching Images...</p>
          </div>
        ) : (
          <PhotoSlideshow results={results} />
        )}
      </div>
    </>
  );
}
